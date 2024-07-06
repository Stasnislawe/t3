from .models import SimpleModel
import xlrd
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True


class UploadingModel(object):
    model = SimpleModel

    def __init__(self, data):
        data = data
        self.upload_file = data.get("file")
        self.request_user = data.get("request_user")
        self.parsing()

    def getting_headers(self):
        s = self.s
        headers = dict()
        for column in range(s.ncols):
            value = s.cell(0, column).value
            headers[column] = value
        return headers


    def parsing(self):
        uploaded_file = self.upload_file
        wb = xlrd.open_workbook(file_contents=uploaded_file.read())
        s = wb.sheet_by_index(0)
        self.s = s

        headers = self.getting_headers()

        model_bulk_list = list()
        for row in range(1, s.nrows):
            row_dict = {}
            for column in range(s.ncols):
                value = s.cell(row, column).value
                field_name = headers[column]

                if field_name == "id" and not value:
                    continue

                if field_name == "create_time":
                    value = str(s.cell(row, column).value)
                    value = value.replace("«", "")
                    value = value.replace("»", "")

                row_dict[field_name] = value
                row_dict['user'] = self.request_user

            model_bulk_list.append(SimpleModel(**row_dict))

        SimpleModel.objects.bulk_create(model_bulk_list)
        return True