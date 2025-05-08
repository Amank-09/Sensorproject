# import sys module interacts with the python interpreter,  lets Python programs interact directly with the Python runtime environment.
#  using it to get details about exceptions (like the file name and line number where the error happened).
import sys

# formats detailed exception info (file name + line number + error).
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message




# Whenever we have to handle exception we can directly call this customexception class.
# lets you raise and print exceptions in a way that's much more helpful for debugging!
class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail = error_detail
        )

    def __str__(self):
        return self.error_message