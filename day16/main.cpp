#include <iostream>
#include <filesystem>
#include <fstream>

auto inPath = "day16/test";

enum Direction {
    RIGHT,
    UP,
    LEFT,
    DOWN
};

struct Pos2d {
    int x, y;
};

struct Grid {
    char* data;
    std::vector<char*> rows;
    int maxRow;
    int maxCol;

    bool inBounds(int col, int row) {
        return col >= 0 && col < maxCol && row >= 0 && row < maxRow;
    }

    char get(int col, int row) {
        return rows[row][col];
    }

    static Grid makeUniform(int maxRow, int maxCol) {
        Grid ret;

        for (int i = 0; i < maxRow; i++) {
            ret.rows.push_back(new char[maxCol]);
        }

        ret.maxRow = maxRow;
        ret.maxCol = maxCol;

        return ret;
    }

    static Grid makeFromStr(char* str) {
        Grid ret;
        ret.data = str;

        for (char* i = str; *i != '\0'; i++) {
            if (*i == '\n') {
                ret.rows.emplace_back(i);
            }
        }

        ret.maxRow = ret.rows.size() - 1;

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
};

void main() {
    std::ifstream file(inPath);
    auto size = std::filesystem::file_size(inPath);
    std::vector<char> contents(size);
    file.read(contents.data(), contents.size());

    std::vector<char> energized(size);

    Grid g = Grid::makeFromStr(contents.data());
    Grid energized = Grid::makeUniform(g.maxRow, g.maxCol);
}