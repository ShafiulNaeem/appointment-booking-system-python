class ValidationRules:
    @staticmethod
    def validate(data, rules):
        errors = {}
        for field, rules in rules.items():
            value = data.get(field)
            if not value:
                # skip validation if the field is not present in the data
                continue
            
            for rule in rules:
                if rule == "required" and not value:
                    errors[field] = f"{field} is required"
                elif rule == "string" and not isinstance(value, str):
                    errors[field] = f"{field} must be a string"
                elif rule == "integer" and not isinstance(value, int):
                    errors[field] = f"{field} must be an integer"
                elif rule == "numeric" and not isinstance(value, (int, float)):
                    errors[field] = f"{field} must be numeric"
                elif rule.startswith("max:") and len(value) > int(rule.split(":")[1]):
                    errors[field] = f"{field} must be at most {rule.split(':')[1]} characters long"
                elif rule.startswith("min:") and len(value) < int(rule.split(":")[1]):
                    errors[field] = f"{field} must be at least {rule.split(':')[1]} characters long"
                elif rule == "email" and "@" not in value:
                    errors[field] = f"{field} must be a valid email address"
                
                elif rule == "file":
                    if not hasattr(value, "filename"):
                        errors[field] = f"{field} must be a file"

                elif rule == "image":
                    if not hasattr(value, "filename") or not value.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                        errors[field] = f"{field} must be an image file (png, jpg, jpeg)"

                elif rule.startswith("extension:"):
                    allowed = tuple(rule.split(":")[1].split(","))
                    if not value.filename.lower().endswith(allowed):
                        errors[field] = f"{field} must have one of these extensions: {', '.join(allowed)}"

                elif rule.startswith("max_size:"):
                    max_size = int(rule.split(":")[1])
                    file_data = value.stream.read()
                    value.stream.seek(0) 
                    if len(file_data) > max_size:
                        errors[field] = f"{field} must be less than {max_size} bytes"

                elif rule.startswith("min_size:"):
                    min_size = int(rule.split(":")[1])
                    file_data = value.stream.read()
                    value.stream.seek(0) 
                    if len(file_data) < min_size:
                        errors[field] = f"{field} must be at least {min_size} bytes"

                
        return errors if errors else None
