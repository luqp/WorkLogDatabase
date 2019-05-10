class Printer():
    
    @classmethod
    def added_successfully(cls):
        print("Dada were added successfully")

    @classmethod
    def show_error_of_data(cls):
        print("Data didn't lunch...")
    
    @classmethod
    def show_optional_value(cls):
        print("This is a optional value, you can scape it:")
    
    @classmethod
    def print_menu(cls):
        print("ADD or VIEW?")

    @classmethod
    def print_information(cls, group):
        for item in group:
            print(item)
