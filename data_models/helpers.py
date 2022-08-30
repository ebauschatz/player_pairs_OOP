class Helpers:
    @staticmethod
    def get_valid_numeric_input(input_type):
        valid_input = False
        while valid_input is False:
            user_value = input(f'Please enter the number of {input_type} for this game: ')
            if user_value.isnumeric() is True:
                return int(user_value)