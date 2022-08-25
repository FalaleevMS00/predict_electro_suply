import src

input_path = "data/raw/Neftebaza.xlsx"
output_path = "data/interim/fix.xlsx"

if __name__ == "__main__":
    src.clean_data(input_path, output_path)


