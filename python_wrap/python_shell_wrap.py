import argparse

def process_input(input_value):
    print(f"Input value is: {input_value}")

def process_dir():
    print("Directory flag is set. Performing directory-related processing.")

def process_number(number_value):
    print(f"Number value is: {number_value}")

def main():
    parser = argparse.ArgumentParser(description='Shell Command Tool')
    
    # Define all possible options with short and long forms
    parser.add_argument('-i', '--input', type=str, action='store', help='Specify the input value')
    parser.add_argument('-d', '--dir', type=bool, action='store_true', help='Perform directory-related processing')
    parser.add_argument('-n', '--number', type=int, action='store', help='Specify a number value')  # Integer type argument
    args = parser.parse_args()

    # Process each option
    if args.input:
        process_input(args.input)
    
    if args.dir:
        process_dir()
    
    if args.number is not None:
        process_number(args.number)

if __name__ == '__main__':
    main()
