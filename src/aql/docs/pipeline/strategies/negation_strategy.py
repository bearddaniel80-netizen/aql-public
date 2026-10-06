from .base import BaseStrategy

class NegationStrategy(BaseStrategy):
    def create_query(self, lst):
        negation_operator = []

        for item in lst:
            name = item["name"]
            negation_template = []

            for operator_template in item["template"]:
                if "BETWEEN" in operator_template:
                    t = operator_template.replace("BETWEEN", "NOT BETWEEN")
                
                elif "IN" in operator_template and "CONTAINS" not in operator_template:
                    t = operator_template.replace("IN", "NOT IN")
                
                t = operator_template.replace("WHERE", "WHERE NOT")
                    
                negation_template.append(t)

            entry = self.copy_object(item, negation_template, name, "NOT")

            negation_operator.append(entry)


        lst.extend(negation_operator)