class File:
    def __init__(self, name, fileType, parent=None):
        self.name = name
        self.fileType = fileType
        self.content = []
        self.children = []
        self.parent = parent

    def addFile(self, file):
        self.children.append(file)
        file.parent = self

    def addContext(self, file):
        self.content.append(file)

    def save_children_name(self):
        children_name_list = []
        for child in self.children:
            children_name_list.append(child.name)
        return children_name_list

    def removeChild(self, name):
        for child in self.children:
            if name == child.name:
                index = self.children.index(child)
        self.children.pop(index)


class System:
    def __init__(self):
        self.currentAccount = None
        self.root = File("root", "directory")
        self.currentDirectory = self.root
        self.accounts = [{"name": "root", "chmod": 3}, {"name": "admin", "chmod": 2}, {"name": "user", "chmod": 1}]

    def su(self, username):
        check = False
        for item in self.accounts:
            if username == item["name"]:
                self.currentAccount = item
                print(f"You have switched to {username}")
                check = True
                break
        if not check:
            print("Invalid account name")

    def pwd(self):
        if self.currentAccount:
            way = []
            node = self.currentDirectory
            while node:
                way.append(node.name)
                node = node.parent
            path = '/' + '/'.join(reversed(way))
            return path
        else:
            print("Please login first.")

    def mkdir_relative_path(self, relative_path):
        if self.currentAccount:
            check = True
            current_directory = self.currentDirectory
            paths = relative_path.split('/')
            if ' ' in paths:
                print("Invalid address.")
            else:
                name_directory = paths[len(paths) - 1]
                for i in range(0, len(paths) - 1):
                    children_name = current_directory.save_children_name()
                    if paths[i] in children_name:
                        for child in current_directory.children:
                            if paths[i] == child.name:
                                current_directory = child
                    else:
                        print(f"The {paths[i]} is not exited.")
                        check = False
                        break
                if check:
                    new_directory = File(name_directory, "directory")
                    current_directory.addFile(new_directory)
                    print(f"{name_directory} was added.")
        else:
            print("Please login first.", end="")

    def rmkdir_relative_path(self, relative_path):
        if self.currentAccount:
            check = True
            current_directory = self.currentDirectory
            paths = relative_path.split('/')
            if ' ' in paths:
                print("Invalid syntax.")
            else:
                name_directory = paths[len(paths) - 1]
                for i in range(0, len(paths) - 1):
                    children_name = current_directory.save_children_name()
                    if paths[i] in children_name:
                        for child in current_directory.children:
                            if paths[i] == child.name:
                                current_directory = child
                    else:
                        print(f"The {paths[i]} is not exited.")
                        check = False
                        break
                if check:
                    current_directory.removeChild(name_directory)
                    print(f"{name_directory} was deleted.")
        else:
            print("Please login first.", end="")

    def mkdir_absolute_path(self, absolute_path):
        if self.currentAccount:
            check = True
            current_directory = self.root
            paths = absolute_path.split('/')
            if ' ' in paths:
                print("Invalid address.")
            elif paths[1] != self.root.name:
                print("Invalid address.")
            else:
                name_directory = paths[len(paths) - 1]
                for i in range(2, len(paths) - 1):
                    children_name = current_directory.save_children_name()
                    if paths[i] in children_name:
                        for child in current_directory.children:
                            if paths[i] == child.name:
                                current_directory = child
                    else:
                        print(f"The {paths[i]} is not exited.")
                        check = False
                        break
                if check:
                    new_directory = File(name_directory, "directory")
                    current_directory.addFile(new_directory)
                    print(f"{name_directory} was added.")
        else:
            print("Please login first.")

    def rmkdir_absolute_path(self, absolute_path):
        if self.currentAccount:
            check = True
            current_directory = self.root
            paths = absolute_path.split('/')
            if ' ' in paths:
                print("Invalid address.")
            elif paths[1] != self.root.name:
                print("Invalid address.")
            else:
                name_directory = paths[len(paths) - 1]
                for i in range(2, len(paths) - 1):
                    children_name = current_directory.save_children_name()
                    if paths[i] in children_name:
                        for child in current_directory.children:
                            if paths[i] == child.name:
                                current_directory = child
                    else:
                        print(f"The {paths[i]} is not exited.")
                        check = False
                        break
                if check:
                    current_directory.removeChild(name_directory)
                    print(f"{name_directory} was deleted.")
        else:
            print("Please login first.")

    def touch(self, name):
        if self.currentAccount:
            new_file = File(name, "file")
            self.currentDirectory.addContext(new_file)
            print(f"{name} is added.")
        else:
            print("Please login first.")

    def cd(self, name):
        if self.currentAccount:
            check = False
            if name == "..":
                if self.currentDirectory.parent is None:
                    check = True
                else:
                    self.currentDirectory = self.currentDirectory.parent
                    check = True
            else:
                for child in self.currentDirectory.children:
                    if name == child.name:
                        self.currentDirectory = child
                        check = True
            if check is False:
                print(f"{name} is not existed.")
        else:
            print("Please login first.")

    def ls(self):
        current_directory = self.currentDirectory
        for child in current_directory.children:
            file_count = len(child.content)
            print(f"{child.name} => file number: {file_count}")

    def cp(self, absolute_path):
        if self.currentAccount:
            check = True
            current_directory = self.root
            temp_dir = self.root
            paths = absolute_path.split('/')
            count_root_name = paths.count(self.root.name)
            if ' ' in paths:
                print("Invalid address.")
            elif paths[1] != self.root.name:
                print("Invalid address.")
            elif count_root_name != 2:
                print("Invalid address.")
            else:
                index_second_root = paths.index(self.root.name, paths.index(self.root.name) + 1)
                first_address = paths[2:index_second_root]
                second_address = paths[index_second_root + 1:]
                if first_address:
                    for i in range(len(first_address)):
                        children_name = current_directory.save_children_name()
                        if first_address[i] in children_name:
                            for child in current_directory.children:
                                if first_address[i] == child.name:
                                    current_directory = child
                        else:
                            print(f"The {paths[i]} is not exited.")
                            check = False
                            break
                    if second_address:
                        for i in range(len(second_address)):
                            children_name = temp_dir.save_children_name()
                            if second_address[i] in children_name:
                                for child in temp_dir.children:
                                    if second_address[i] == child.name:
                                        temp_dir = child
                            else:
                                print(f"The {paths[i]} is not exited.")
                                check = False
                                break
                    else:
                        pass
                    if check:
                        name_dir = current_directory.name
                        content = current_directory.content
                        new_dir = File(name_dir, "directory")
                        for item in content:
                            new_dir.addContext(item)
                        temp_dir.addFile(new_dir)
                        print(f"{new_dir} is copied.")
                else:
                    print("Invalid syntax.")
        else:
            print("Please login first.")

    def mv(self, absolute_path):
        if self.currentAccount:
            check = True
            current_directory = self.root
            temp_dir = self.root
            paths = absolute_path.split('/')
            count_root_name = paths.count(self.root.name)
            if ' ' in paths:
                print("Invalid address1.")
            elif paths[1] != self.root.name:
                print("Invalid address2.")
            elif count_root_name != 2:
                print("Invalid address3.")
            else:
                index_second_root = paths.index(self.root.name, paths.index(self.root.name) + 1)
                first_address = paths[2:index_second_root]
                second_address = paths[index_second_root + 1:]
                if first_address:
                    for i in range(len(first_address)):
                        children_name = current_directory.save_children_name()
                        if first_address[i] in children_name:
                            for child in current_directory.children:
                                if first_address[i] == child.name:
                                    current_directory = child
                        else:
                            print(f"The {paths[i]} is not exited.")
                            check = False
                            break
                    if second_address:
                        for i in range(len(second_address)):
                            children_name = temp_dir.save_children_name()
                            if second_address[i] in children_name:
                                for child in temp_dir.children:
                                    if second_address[i] == child.name:
                                        temp_dir = child
                            else:
                                print(f"The {paths[i]} is not exited.")
                                check = False
                                break
                    else:
                        pass
                    if check:
                        name_dir = current_directory.name
                        content = current_directory.content
                        new_dir = File(name_dir, "directory")
                        for item in content:
                            new_dir.addContext(item)
                        temp_dir.addFile(new_dir)
                        delete_list = paths[1:index_second_root]
                        delete_address = '/' + '/'.join(delete_list)
                        self.rmkdir_absolute_path(delete_address)
                        print(f"{delete_list[-1]} is moved.")

                else:
                    print("Invalid syntax4.")
        else:
            print("Please login first.")
    def find(self, absolute_path, type, name, search):
        if self.currentAccount:
            check = True
            current_directory = self.root
            paths = absolute_path.split('/')
            if ' ' in paths:
                print("Invalid address.")
            elif paths[1] != self.root.name:
                print("Invalid address.")
            else:
                name_directory = paths[len(paths) - 1]
                for i in range(2, len(paths) - 1):
                    children_name = current_directory.save_children_name()
                    if paths[i] in children_name:
                        for child in current_directory.children:
                            if paths[i] == child.name:
                                current_directory = child
                    else:
                        print(f"The {paths[i]} is not exited.")
                        check = False
                        break
                if check:
                    pass
        else:
            print("Please login first.")
    def print_prent(self):
        parent_name = []
        current_dir = self.currentDirectory
        while current_dir.parent:
            parent_name.append(current_dir.parent.name)
            current_dir = current_dir.parent
        print(parent_name)

    def sp(self, absolute_path):
        if self.currentAccount:
            check = True
            current_directory = self.root
            temp_dir = self.root
            paths = absolute_path.split('/')
            count_root_name = paths.count(self.root.name)
            if ' ' in paths:
                print("Invalid address.")
            elif paths[1] != self.root.name:
                print("Invalid address.")
            elif count_root_name != 2:
                print("Invalid address.")
            else:
                index_second_root = paths.index(self.root.name, paths.index(self.root.name) + 1)
                first_path = paths[1:index_second_root - 1]
                second_path = paths[index_second_root: len(paths) - 1]
                first_address = paths[2:index_second_root]
                second_address = paths[index_second_root + 1:]
                if first_address:
                    for i in range(len(first_address)):
                        children_name = current_directory.save_children_name()
                        if first_address[i] in children_name:
                            for child in current_directory.children:
                                if first_address[i] == child.name:
                                    current_directory = child
                        else:
                            print(f"The {paths[i]} is not exited.")
                            check = False
                            break
                    if second_address:
                        for i in range(len(second_address)):
                            children_name = temp_dir.save_children_name()
                            if second_address[i] in children_name:
                                for child in temp_dir.children:
                                    if second_address[i] == child.name:
                                        temp_dir = child
                            else:
                                print(f"The {paths[i]} is not exited.")
                                check = False
                                break
                    else:
                        pass
                    if check:
                        if first_path and second_path:
                            if len(first_path) >= len(second_path):
                                a = first_path
                                b = second_path
                                a.reverse()
                                b.reverse()
                                for item in a:
                                    if item in b:
                                        result = item
                                        break
                            else:
                                a = second_path
                                b = first_path
                                a.reverse()
                                b.reverse()
                                for item in a:
                                    if item in b:
                                        result = item
                                        break
                            print(result)
                else:
                    print("Invalid syntax.")
        else:
            print("Please login first.")

    def sz(self):
        print(f"dir: {len(self.currentDirectory.children)}")
        print(f"fl: {len(self.currentDirectory.content)}")

    def find(self):
        pass


# main
def help():
    print("Available commands:")
    print("su name: switch to the account with the given name")
    print("pwd: the path of root to current node.")
    print("mkdir relative_path/name: add directory in relative path.")
    print("mkdir /absolute_path/name: add directory in absolute path.")
    print("touch name: add a file in current directory.")
    print("cd name: change directory to name.")



def check_address_relative(command):
    check = False
    words = command.split(" ", 1)
    try:
        for item in words[1]:
            if item == " ":
                check = True
                break
        return check
    except:
        print("Invalid syntax")


system = System()
print("Welcome to the file system simulator")
print("Type help for a list of commands")
while True:
    if system.currentAccount:
        name = system.currentAccount["name"]
        print(f"{name}: ", end="")
        print(system.pwd(), end="")
        print(" :> ", end="")
    else:
        print("> ", end="")
    command = input()
    word = command.split()
    if len(word) == 0:
        continue
    if word[0] == "su":
        system.su(word[1])
    elif word[0] == "sp":
        system.sp(word[1])
    elif word[0] == "sz":
        system.sz()
    elif word[0] == "cd":
        system.cd(word[1])
    elif word[0] == "ls":
        system.ls()
    elif word[0] == "pwd":
        system.pwd()
    elif word[0] == "mkdir":
        if system.currentAccount["chmod"] >= 2:
            if check_address_relative(command):
                print("Invalid address.")
            elif len(word) == 1:
                print("Invalid address.")
            else:
                if word[1][0] == '/':
                    system.mkdir_absolute_path(word[1])
                else:
                    system.mkdir_relative_path(word[1])
        else:
            print("You do not have access.")
    elif word[0] == "rmkdir":
        if system.currentAccount["chmod"] >= 2:
            if check_address_relative(command):
                print("Invalid address.")
            elif len(word) == 1:
                print("Invalid address.")
            else:
                if word[1][0] == '/':
                    system.rmkdir_absolute_path(word[1])
                else:
                    system.rmkdir_relative_path(word[1])
        else:
            print("You do not have access.")
    elif word[0] == "cp":
        if system.currentAccount["chmod"] >= 2:
            system.cp(word[1])
        else:
            print("You do not have access.")
    elif word[0] == "mv":
        if system.currentAccount["chmod"] >= 2:
            system.mv(word[1])
        else:
            print("You do not have access.")
    elif word[0] == "touch":
        if system.currentAccount["chmod"] >= 2:
            if len(word) == 1:
                print("Write your file name.")
            elif len(word) == 2:
                system.touch(word[1])
            else:
                print("Invalid syntax.")
        else:
            print("You do not have access.")
    elif word[0] == "find":
        if len(word) == 5:
            absolute_path = word[1]
            type = word[2]
            name = word[3]
            search = word[4]
        else:
            print("Invalid syntax.")
    elif word[0] == "help":
        help()
    elif word[0] == "exit":
        print("Goodbye")
        break
    else:
        print("Invalid syntax.")
