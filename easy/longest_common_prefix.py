def longestCommonPrefix(self, lista: List[str]) -> str:
        if not lista :return ""
        for idx,x in enumerate(lista):
            if idx == 0:
                prefix = x
            else:
                while not x.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        break
        return prefix
                