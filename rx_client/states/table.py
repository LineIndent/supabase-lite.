from .base import Base


class TableState(Base):
    def paginate(self):
        start = self.offset
        end = start + self.current_limit
        self.paginated_data = self.main_data[start:end]
        self.current_page = (self.offset // self.current_limit) + 1

    def delta_limit(self, limit: str):
        self.current_limit = int(limit)
        self.offset = 0
        self.total_pages = (
            self.number_of_rows + self.current_limit - 1
        ) // self.current_limit
        self.paginate()

    def previous(self):
        if self.offset >= self.current_limit:
            self.offset -= self.current_limit
        else:
            self.offset = 0

        self.paginate()

    def next(self):
        if self.offset + self.current_limit < self.number_of_rows:
            self.offset += self.current_limit

        self.paginate()
