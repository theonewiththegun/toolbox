import os


def list_to_scalar(input_list):
    """
    This is a helper function, that turns a list into a scalar if its length is 1.
    """
    if len(input_list) == 1:
        return input_list[0]
    else:
        return input_list


class Folder:
    def __init__(self, path):
        self.abs_path = os.path.abspath(path)
        self.basename = os.path.basename(self.abs_path)

    def file_names(self, *args):
        """
        You can pass indices of files names of which you want to get through *args.
        """
        excluded_file_names = ['.DS_Store', '.gitignore']
        current_file_names_snapshot_base = os.listdir(self.abs_path)
        current_file_names_snapshot = [f for f in current_file_names_snapshot_base if f not in excluded_file_names]
        if args:
            result_list = []
            for file_index in args:
                result_list.append(
                    current_file_names_snapshot[file_index]
                )
            # если индексами выбран только один элемент, то вернуть скаляр
            return list_to_scalar(result_list)
        else:
            # если никакой индекс не задан, то вернуть список
            return current_file_names_snapshot

    def file_paths(self, *args):
        """
        You can pass indices of files names of which you want to get through *args.
        """
        current_file_names_snapshot = self.file_names()
        if args:
            result_list = []
            for file_index in args:
                result_list.append(
                    os.path.join(self.abs_path, current_file_names_snapshot[file_index])
                )
            # если индексами выбран только один элемент, то вернуть скаляр
            return list_to_scalar(result_list)
        else:
            # если никакой индекс не задан, то вернуть список
            return [os.path.join(self.abs_path, x) for x in current_file_names_snapshot]

    def files_count(self):
        return len(self.file_paths())
