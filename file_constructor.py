import json


class FileConstructor:
    def __init__(self, filename_source, filename_final, mode):
        self.filename_source = filename_source
        self.filename_final = filename_final
        self.mode = mode

    def __enter__(self):
        self.file_source = open(self.filename_source, "r")
        self.file_final = open(self.filename_final, self.mode)
        return {"file_source": self.file_source, "file_final": self.file_final}

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file_source.close()
        self.file_final.close()


if __name__ == "__main__":
    source = "put_the_source_file_name_here"
    final = "put_the_final_file_name_here"

    with FileConstructor(source, final, "w") as construct:
        data_to_be_written = "any_format_of_data_you_want_to_write_to_final_file"

        temp_data = data_to_be_written.copy()
        """
            Put your function to process data here, from source format to final format.
            Utilize temp_data, construct["file_source"], construce["file_final"] if necessary.
            Use read or write method in utilizing the data.
        """
        data_to_be_written = temp_data.copy()

        data_to_be_written = json.dumps(data_to_be_written)
        construct["file_final"].write(data_to_be_written)
