//
// Created by developer on 4/24/20.
//
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "item.h"

using namespace std;

std::string& ltrim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    str.erase(0, str.find_first_not_of(chars));
    return str;
}

std::string& rtrim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    str.erase(str.find_last_not_of(chars) + 1);
    return str;
}

std::string& trim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    return ltrim(rtrim(str, chars), chars);
}

vector<string> split (const string &s, char delim) {
    vector<string> result;
    stringstream ss (s);
    string item;

    while (getline (ss, item, delim)) {
        result.push_back (item);
    }

    return result;
}

ostream & operator << (ostream & os, const item & it) {
    os << "item('" << it._id << "', " << it._cost << ", " << it._quant << ")";
}

bool loadItemsFromCSV(const std::string & filename, itemVector & vec) {
    cout << "Loading dataset from file " << filename << endl;

    vec.clear();

    ifstream csvFile(filename);

    if (csvFile.is_open()) {
        string line;

        while (getline(csvFile, line)) {
            auto tuple = split(line, ',');
            auto id = trim(tuple[0], "\"");
            auto cost = atof(tuple[1].c_str());
            auto quant = atoi(tuple[2].c_str());

            vec.push_back(item(id, cost, quant));
        }
    }

    return (vec.size() > 0);
}
