import os

class Printer():
    
    STYLE_END = "\033[0m"
    YELLOW_GRAY = "\x1b[1;34m"

    @classmethod
    def clean_screen(cls):
        os.system("cls" if os.name == "nt" else "clear")

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
    def prompting_by_delete(cls):
        print("Are you sure?")

    @classmethod
    def show_result(cls, result):
        value = "was deleted" if result else "no deleted"
        print(f"The instance {value}")

    @classmethod
    def print_one_item(cls, item):
        cls.clean_screen()
        date = item.date.strftime("%A %B %d, %Y %I:%M%p")
        print(f"{date}")
        print(f"Name: {item.name}")
        print(f"Task: {item.task_name}")
        print(f"Time spend: {item.time_work}")
        print(f"Notes: {item.notes}")       

    @classmethod
    def print_information(cls, group, selected):
        cls.clean_screen()
        ideal_size = 20
        for in_group in group:
            id_item, item = in_group
            if id_item == selected.id:
                style = "> "
            else:
                style = ""
            to_print = cls.format_to_display(item, ideal_size)
            print(f"{style}{to_print}")
            print("-" * (ideal_size + 5) * len(item))

    @classmethod
    def format_to_display(cls, values, ideal_size):
        to_print = ""
        for value in values:
            if len(value) != ideal_size:
                value = cls.convert_to_len10(value, ideal_size)
            to_print += value + " " * 5
        return to_print

    @classmethod
    def convert_to_len10(cls, value, ideal_size):
        size = len(value)
        if size < ideal_size:
            value += " " * (ideal_size - size)
        elif size > ideal_size:
            value = value[:ideal_size - 3]
            value += "." * 3
        return value
            

