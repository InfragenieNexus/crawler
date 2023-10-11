from datetime import datetime


class NameGenerator:
    """Class to generate a name for the output file"""

    @staticmethod
    def generate_name_with_timestamp(name, *filters) -> str:
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%H-%M")
        filter_str = "_".join(str(filter) for filter in filters if filter is not None)

        result = f"output/{name}_{filter_str}_{timestamp}"

        return result
