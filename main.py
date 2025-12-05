from sequence_adn import ADN
def linear_search(adn_list, target):
    target = list(target)
    chunksize = len(target)
    result = []

    for i in range(len(adn_list) - chunksize + 1):
        if adn_list[i:i+chunksize] == target:
            result.append(i)  # append index to results

    return result


def simple_compress(adn_list):
    compressed = []
    count = 1
    for adn_index in range(1,len(adn_list)):
        if adn_list[adn_index-1] == adn_list[adn_index]:
            count += 1
        else:
            compressed.append((adn_list[adn_index-1], count))
            count = 1
    return compressed
print(simple_compress(ADN))
print(linear_search(ADN, "AAATTCG"))