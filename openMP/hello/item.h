//
// Created by developer on 4/24/20.
//

#ifndef HELLO_ITEM_H
#define HELLO_ITEM_H

#include <string>
#include <vector>

class item {
public:
    item(std::string id, double cost, int quant)
            : _id(id), _cost(cost), _quant(quant)
    {
    }

    const std::string & id() const {
        return _id;
    }

    const double cost() const {
        return _cost;
    }

    const int quant() const {
        return _quant;
    }

    friend std::ostream & operator << (std::ostream & os, const item & it);

private:
    std::string _id;    // Identifier
    double      _cost;  // Cost
    int         _quant; // Quantity
};

using itemVector = std::vector<item>;

/**
 * Load items from file in CSV format.
 * @param filename string containing path of file.
 * @return true if file was loaded.
 */
bool loadItemsFromCSV(const std::string & filename, itemVector & vec);

#endif //HELLO_ITEM_H
