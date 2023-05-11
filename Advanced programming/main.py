def read_intervals(filepath):
    """
    Read a file containing intervals and return them as a list of tuples.

    Args:
        filepath (str): the path to the file

    Returns:
        list of tuples: the intervals
    """
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
    return [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]


def binary_search(intervals, target):
    """
    Search for a target value in a list of intervals using binary search.

    Args:
        intervals (list of tuples): the intervals to search
        target (int): the value to search for

    Returns:
        int: the index of the interval that contains the target value, or the index of the first interval that starts after the target value if the target value is not found
    """
    left = 0
    right = len(intervals) - 1
    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][1] < target:
            left = mid + 1
        elif intervals[mid][0] > target:
            right = mid - 1
        else:
            return mid
    return left


def similarity_between_lines(line1, line2):
    """
    Calculate the Jaccard similarity between two lines.

    Args:
        line1 (list of ints): the first line
        line2 (list of ints): the second line

    Returns:
        float: the Jaccard similarity between the two lines
    """
    intervals1 = [tuple(line1[i:i+2]) for i in range(0, len(line1), 2)]
    intervals2 = [tuple(line2[i:i+2]) for i in range(0, len(line2), 2)]

    count = 0
    j = 0
    for interval1 in intervals1:
        j = binary_search(intervals2, interval1[0])
        if j == len(intervals2):
            break
        if interval1[1] >= intervals2[j][0]:
            count += 1
    similarity = count / max(len(intervals1), len(intervals2))
    return similarity


def symmetric_similarity(set_1, set_2):
    """
    Calculate the symmetric Jaccard similarity between two sets of lines.

    Args:
        lines_set1 (set of tuples): the set of lines in the first file
        lines_set2 (set of tuples): the set of lines in the second file

    Returns:
        float: the symmetric Jaccard similarity between the two sets of lines
    """
    sim12 = similarity_between_lines(set_1, set_2)
    sim21 = similarity_between_lines(set_2, set_1)
    return (sim12 + sim21) / 2


def similarity(set_1, set_2, outfile):
    """
    Calculate the similarity between two files.

    Args:
        file1 (str): the path to the first file
        file2 (str): the path to the second file
        outfile (str): the path

    Returns:
        float: the symmetric Jaccard similarity between the two files
    """
    lines_set_1 = read_intervals(set_1)
    lines_set_2 = read_intervals(set_2)

    num_lines_1 = len(lines_set_1)
    num_lines_2 = len(lines_set_2)

    if num_lines_1 != num_lines_2:
        print("Warning: Sets do not contain same amount of lists.")

    similarities = []
    for i, line1 in enumerate(lines_set_1):
        line2 = lines_set_2[i]
        sim = symmetric_similarity(line1, line2)
        similarities.append(sim)

    avg_sim = sum(similarities) / num_lines_1

    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(avg_sim))





