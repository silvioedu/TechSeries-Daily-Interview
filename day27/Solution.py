def courses_to_take(course_to_prereqs):
    return sorted(course_to_prereqs.keys())


if __name__ == '__main__':
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    print(courses_to_take(courses))
    # ['CSC100', 'CSC200', 'CSC300']