#Main script

def read_intervals(filepath):
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
    return [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]

#print(read_intervals('set1.txt'))
#print(read_intervals('set2.txt'))

def similarity_between_lines(line1, line2):
    intervals1 = [tuple(line1[i:i+2]) for i in range(0, len(line1), 2)]
    intervals2 = [tuple(line2[i:i+2]) for i in range(0, len(line2), 2)]
    count = 0
    for interval1 in intervals1:
        for interval2 in intervals2:
            if max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1]):
                count += 1
                break
    similarity = count / max(len(intervals1), len(intervals2))
    return similarity

def symmetric_similarity(set_1, set_2):
    sim12 = similarity_between_lines(set_1, set_2)
    sim21 = similarity_between_lines(set_2, set_1)
    return (sim12 + sim21) / 2


print(symmetric_similarity((2, 5, 11, 17, 22, 37), (3, 8, 18, 20, 24, 26, 29, 33)))
#print(symmetric_similarity((110, 117, 255, 263), (117, 120, 240, 256, 259, 307)))
#print(symmetric_similarity((44, 66, 87, 104, 188, 204), (20, 44, 71, 75, 180, 192, 303, 315)))
#print(symmetric_similarity((2, 33, 47, 56, 90, 99, 301, 312, 554, 707), (7, 35, 45, 58, 101, 119, 1043, 1352)))
