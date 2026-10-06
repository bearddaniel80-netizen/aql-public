class BaseStrategy:
    def copy_object(self, item, template, name, prefix_name):
        entry = {}

        entry["name"] = f"{prefix_name} {name}"
        entry["template"] = template
        self._copy_if_exists("input_type", entry, item)
        self._copy_if_exists("return_type", entry, item)
        self._copy_if_exists("needs_groupby_clause", entry, item)
        
        return entry

    def _copy_if_exists(self, key, entry, item):
        if key in item.keys():
            entry[key] = item[key]
