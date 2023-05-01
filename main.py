#Main script

def read_intervals(filepath):
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
    return [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]



def jaccard_index(set1, set2):
    set1 = set(set1)
    set2 = set(set2)
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / union_size if union_size > 0 else 1.0

def similarity(set_1, set_2, outfile):
    set1_intervals = read_intervals(set_1)
    set2_intervals = read_intervals(set_2)
    jaccard = jaccard_index(set1_intervals, set2_intervals)
    similarity_score = round(1 - jaccard, 2)
    with open(outfile, 'w') as f:
        f.write(str(similarity_score))

print(read_intervals('set1.txt'))