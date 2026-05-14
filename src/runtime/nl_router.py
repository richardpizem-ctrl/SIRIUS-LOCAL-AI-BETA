    def _handle_rule_based(self, text: str):
        """
        Rule-based NL commands for Password Vault 4.0
        """

        # ----------------------------------------------------
        # SAVE PASSWORD
        # ----------------------------------------------------
        # Example: "uloz heslo pre github je 12345"
        if "uloz heslo" in text or "save password" in text:
            try:
                # extract domain
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                # extract password
                match = re.search(r"je ([^\s]+)$", text)
                password = match.group(1) if match else None

                if domain and password:
                    from security_family.password_vault.vault_api import save_password
                    save_password(domain, "default", password)
                    return f"Heslo pre {domain} bolo uložené."
                else:
                    return "Nepodarilo sa extrahovať doménu alebo heslo."
            except Exception as e:
                return f"Chyba pri ukladaní hesla: {e}"

        # ----------------------------------------------------
        # RETRIEVE PASSWORD
        # ----------------------------------------------------
        # Example: "ake je heslo pre github"
        if "ake je heslo" in text or "what is the password" in text:
            try:
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                if domain:
                    from security_family.password_vault.vault_api import retrieve_password
                    entry = retrieve_password(domain)
                    if entry:
                        return f"Heslo pre {domain} je: {entry['password']}"
                    else:
                        return f"Nemám uložené heslo pre {domain}."
                else:
                    return "Nepodarilo sa extrahovať doménu."
            except Exception as e:
                return f"Chyba pri načítaní hesla: {e}"

        # ----------------------------------------------------
        # AUTOFILL PASSWORD (PC)
        # ----------------------------------------------------
        # Example: "vypln heslo pre github"
        if "vypln heslo" in text or "autofill password" in text:
            try:
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                if domain:
                    from security_family.password_vault.vault_api import retrieve_password
                    entry = retrieve_password(domain)
                    if entry:
                        # TODO: integrate with Windows UI Automation
                        return f"Heslo pre {domain} je pripravené na autofill."
                    else:
                        return f"Nemám uložené heslo pre {domain}."
                else:
                    return "Nepodarilo sa extrahovať doménu."
            except Exception as e:
                return f"Chyba pri autofill operácii: {e}"

        # ----------------------------------------------------
        # No match
        # ----------------------------------------------------
        return None
