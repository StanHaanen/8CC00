#Main script

def read_intervals(filepath):
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
    return [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]

def similarity_between_lines(line1, line2):
    intervals1 = [tuple(line1[i:i+2]) for i in range(0, len(line1), 2)]
    intervals2 = [tuple(line2[i:i+2]) for i in range(0, len(line2), 2)]
    
    count = 0
    j = 0
    for interval1 in intervals1:
        while j < len(intervals2) and intervals2[j][1] < interval1[0]:
            j += 1
        if j == len(intervals2):
            break
        if interval1[1] >= intervals2[j][0]:
            count += 1
    similarity = count / max(len(intervals1), len(intervals2))
    return similarity

def symmetric_similarity(set_1, set_2):
    sim12 = similarity_between_lines(set_1, set_2)
    sim21 = similarity_between_lines(set_2, set_1)
    return (sim12 + sim21) / 2

def similarity(set_1, set_2, outfile):
    with open(set_1, 'r') as f:
        lines_set_1 = [tuple(int(bound.strip('[], ')) for bound in line.strip().split(',')) for line in f.readlines()]

    with open(set_2, 'r') as f:
        lines_set_2 = [tuple(int(bound.strip('[], ')) for bound in line.strip().split(',')) for line in f.readlines()]

    num_lines_1 = len(lines_set_1)
    num_lines_2 = len(lines_set_2)

    if num_lines_1 != num_lines_2:
        print("Warning: Sets do not contain same amount of lists.")

    similarities = []
    for i in range(num_lines_1):
        sim12 = similarity_between_lines(lines_set_1[i], lines_set_2[i])
        sim21 = similarity_between_lines(lines_set_2[i], lines_set_1[i])
        sim = (sim12 + sim21) / 2
        similarities.append(sim)

    avg_sim = sum(similarities) / num_lines_1

    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(avg_sim))

