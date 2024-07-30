from datetime import datetime
import time

def function_logger(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")

            result = func(*args, **kwargs)

            end_time = datetime.now()
            end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")

            execution_time = end_time - start_time

            args_str = str(args) if args else '-'
            kwargs_str = str(kwargs) if kwargs else '-'
            result_str = str(result) if result else '-'

            log_info = f"{func.__name__}\n{start_time_str}\n{args_str}, {kwargs_str}\n{result_str}\n{end_time_str}\n{execution_time}\n"

            with open(file_path, 'a') as file:
                file.write(log_info)

            return result
        return wrapper
    return decorator

@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    greeting_format('John')
