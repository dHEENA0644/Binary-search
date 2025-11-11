import json
import os

class ContactNode:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.left = None
        self.right = None


class BSTContactDirectory:
    def __init__(self):
        self.root = None
        self.load_contacts()

    def insert(self, name, phone, email):
        self.root = self._insert(self.root, name, phone, email)
        self.save_contacts()

    def _insert(self, node, name, phone, email):
        if not node:
            return ContactNode(name, phone, email)
        if name.lower() < node.name.lower():
            node.left = self._insert(node.left, name, phone, email)
        elif name.lower() > node.name.lower():
            node.right = self._insert(node.right, name, phone, email)
        else:
            node.phone = phone
            node.email = email
        return node

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if not node:
            return None
        if name.lower() == node.name.lower():
            return node
        elif name.lower() < node.name.lower():
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def delete(self, name):
        self.root = self._delete(self.root, name)
        self.save_contacts()

    def _delete(self, node, name):
        if not node:
            return node
        if name.lower() < node.name.lower():
            node.left = self._delete(node.left, name)
        elif name.lower() > node.name.lower():
            node.right = self._delete(node.right, name)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.name, node.phone, node.email = temp.name, temp.phone, temp.email
            node.right = self._delete(node.right, temp.name)
        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def display(self):
        contacts = []
        self._inorder(self.root, contacts)
        return contacts

    def _inorder(self, node, contacts):
        if node:
            self._inorder(node.left, contacts)
            contacts.append({"name": node.name, "phone": node.phone, "email": node.email})
            self._inorder(node.right, contacts)

    def save_contacts(self):
        contacts = self.display()
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as f:
                contacts = json.load(f)
                for c in contacts:
                    self.insert(c["name"], c["phone"], c["email"])
