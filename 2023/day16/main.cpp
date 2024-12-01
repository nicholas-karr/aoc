#include <iostream>
#include <filesystem>
#include <fstream>
#include <cassert>

auto inPath = "/Users/nickk/dev/aoc/day16/input";

#define RIGHT 0
#define UP 90
#define LEFT 180
#define DOWN 270

struct Pos2d {
    int x, y;
};

Pos2d nextDir[] = {
    { 1, 0 },
    { 0, -1 },
    { -1, 0 },
    { 0, 1 }
};

struct Grid {
    char* data;
    std::vector<char*> rows;
    int maxRow;
    int maxCol;

    bool inBounds(int col, int row) {
        return col >= 0 && col < maxCol && row >= 0 && row < maxRow;
    }

    char get(int col, int row, char defaultVal = '.') {
        if (!inBounds(col, row)) {
            return defaultVal;
        }
        return rows[row][col];
    }

    void set(int col, int row, char v) {
        rows[row][col] = v;
    }

    static Grid makeUniform(int maxRow, int maxCol, char defaultVal = '.') {
        Grid ret;

        for (int i = 0; i < maxRow; i++) {
            ret.rows.push_back(new char[maxCol]);
            std::fill(ret.rows.back(), ret.rows.back() + maxCol, defaultVal);
        }

        ret.maxRow = maxRow;
        ret.maxCol = maxCol;

        return ret;
    }

    static Grid makeFromStr(char* str) {
        Grid ret;
        ret.data = str;
        ret.rows.emplace_back(str);

        for (char* i = str; *i != '\0'; i++) {
            if (*i == '\n') {
                ret.rows.emplace_back(i + 1);
            }
        }

        ret.maxCol = ret.rows[1] - ret.rows[0] - 1;
        ret.maxRow = ret.rows.size();

        return ret;
    }

    int count(char c) {
        int cnt = 0;
        for (int row = 0; row < maxRow; row++) {
            for (int col = 0; col < maxCol; col++) {
                if (get(col, row) == c) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    void print() {
        for (int row = 0; row < maxRow; row++) {
            for (int col = 0; col < maxCol; col++) {
                std::cout << get(col, row, '}');
            }
            std::cout << '\n';
        }
    }

    void clear(char val = '.') {
        for (int row = 0; row < maxRow; row++) {
            for (int col = 0; col < maxCol; col++) {
                set(col, row, val);
            }
        }
    }
};


struct Beam {
    int x, y;
    int dir;

    bool operator==(Beam& rhs) const {
        return x == rhs.x && y == rhs.y && dir == rhs.dir;
    }
};

std::pair<Beam, int> sim(Grid& g, Beam start) {
    static std::vector<Beam> alreadySimulated = {};
    static std::vector<Beam> beams = { start };
    static std::vector<Beam> nextBeamList = {};
    static Grid energized = Grid::makeUniform(g.maxRow, g.maxCol);

    alreadySimulated.clear();
    beams = { start };
    nextBeamList.clear();
    energized.clear();

    std::vector<int> energizedCounts;

    while (energizedCounts.size() < 20 || energizedCounts[energizedCounts.size() - 1] != energizedCounts[energizedCounts.size() - 10]) {
        for (Beam& beam : beams) {
            auto nextPos = nextDir[(int)beam.dir / 90];
            nextPos = { nextPos.x + beam.x, nextPos.y + beam.y };
            auto dir = beam.dir;

            Beam out1 = { -1, -1, -1 };
            Beam out2 = { -1, -1, -1 };

            char next = g.get(nextPos.x, nextPos.y);

            assert(next == '.' || next == '\\' || next == '/' || next == '-' || next == '|');

            if (next == '.') {
                out1 = { nextPos.x, nextPos.y, dir };
            }
            else if (next == '\\') {
                switch (dir) {
                case RIGHT: out1 = { nextPos.x, nextPos.y, DOWN }; break;
                case UP: out1 = { nextPos.x, nextPos.y, LEFT }; break;
                case LEFT: out1 = { nextPos.x, nextPos.y, UP }; break;
                case DOWN: out1 = { nextPos.x, nextPos.y, RIGHT }; break;
                }
            }
            else if (next == '/') {
                switch (dir) {
                case RIGHT: out1 = { nextPos.x, nextPos.y, UP }; break;
                case UP: out1 = { nextPos.x, nextPos.y, RIGHT }; break;
                case LEFT: out1 = { nextPos.x, nextPos.y, DOWN }; break;
                case DOWN: out1 = { nextPos.x, nextPos.y, LEFT }; break;
                }
            }
            else if (next == '|') {
                if (dir == UP || dir == DOWN) {
                    out1 = { nextPos.x, nextPos.y, dir };
                }
                else {
                    out1 = { nextPos.x, nextPos.y, UP };
                    out2 = { nextPos.x, nextPos.y, DOWN };
                }
            }
            else if (next == '-') {
                if (dir == RIGHT || dir == LEFT) {
                    out1 = { nextPos.x, nextPos.y, dir };
                }
                else {
                    out1 = { nextPos.x, nextPos.y, RIGHT };
                    out2 = { nextPos.x, nextPos.y, LEFT };
                }
            }

            if (out1.dir != -1 && g.inBounds(out1.x, out1.y) && std::find(alreadySimulated.begin(), alreadySimulated.end(), out1) == alreadySimulated.end()) {
                nextBeamList.push_back(out1);
                energized.set(out1.x, out1.y, '#');
                alreadySimulated.push_back(out1);
            }
            if (out2.dir != -1 && g.inBounds(out2.x, out2.y) && std::find(alreadySimulated.begin(), alreadySimulated.end(), out2) == alreadySimulated.end()) {
                nextBeamList.push_back(out2);
                energized.set(out2.x, out2.y, '#');
                alreadySimulated.push_back(out2);
            }
        }

        energizedCounts.push_back(energized.count('#'));
        std::swap(beams, nextBeamList);
        nextBeamList.clear();
    }

    //energized.print();
    return { start, energizedCounts.back() };
}

void main() {
    std::ifstream file(inPath);
    auto size = std::filesystem::file_size(inPath);
    std::vector<char> contents(size);
    file.read(contents.data(), contents.size());

    Grid g = Grid::makeFromStr(contents.data());

    std::cout << sim(g, { -1, 0, RIGHT }).second << '\n';

    std::vector<std::pair<Beam, int>> scores;
    for (int i = 0; i < g.maxCol; i++) {
        scores.push_back(sim(g, { i, -1, DOWN }));
        scores.push_back(sim(g, { i, g.maxRow, UP }));
    }
    for (int i = 0; i < g.maxRow; i++) {
        scores.push_back(sim(g, { -1, i, RIGHT }));
        scores.push_back(sim(g, { g.maxCol, i, LEFT }));
    }

    int max = 0;
    for (auto& i : scores) {
        max = std::max(max, i.second);
    }
    std::cout << max;
}