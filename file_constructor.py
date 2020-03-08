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
    source = "packages_from_pergiumrohcom.json"
    final = "product_search.json"

    with FileConstructor(source, final, "w") as construct:
        data_to_be_written = {
            "title": [],
            "tagline": [],
            "date": [],
            "transportations": [],
            "accommodations": [],
            "tags": [],
            "price": [],
            "slashPrice": [],
            "packageName": []
        }

        temp_data = data_to_be_written.copy()
        for source in json.loads(construct["file_source"].read()):
            temp_data["title"].append(source["name"])
            # temp_data["tagline"].append(source["name"])
            temp_data["date"].append(source["departure_date"])
            # temp_data["transportations"].append(source["name"])
            # temp_data["accommodations"].append(source["name"])
            # temp_data["tags"].append(source["name"])
            temp_data["price"].append(source["original_price"])
            temp_data["slashPrice"].append(source["reduced_price"])
            temp_data["packageName"].append(source["rooms"][0]["type"])
        data_to_be_written = temp_data.copy()
        print(data_to_be_written)

        data_to_be_written = json.dumps(data_to_be_written)
        print(type(data_to_be_written))
        construct["file_final"].write(data_to_be_written)