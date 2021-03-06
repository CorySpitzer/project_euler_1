from pe1_library import find_sum, Multiples

def main():
    # print('main called')
    print('Functionally we get: ' + str(find_sum()))
    print('Objectively we get: ' + str(Multiples(3,5,1000).sum()))

# only execute main() if the script is being run directly, but not imported;
# __name__ is set to '__main__' only if we run 'python pe1.py',
# but not with 'import pe1'
# (see stackoverflow.com/questions/419163/what-does-if-name-main-do for details)
if __name__ == '__main__':
    main()
