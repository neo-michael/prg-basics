class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def print(self):
        print(f"{self.username}'s posts:")
        i = 1
        for post in self.posts:
            print(f"\t{i}. {post}")
            i += 1

a1 = SocialMediaProfile("123")

a1.add_post("123412421")
a1.add_post("hroibrboe3w")
a1.print()