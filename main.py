from pyscript import document

grade_7 = {"Ana Santos", "Ben Reyes", "Carla Lim"}
grade_8 = {"Dario Cruz", "Elena Tan", "Felix Go"}
grade_9 = {"Gina Diaz", "Hugo Ramos", "Isabel Co"}
grade_10 = {"Jared Uy", "Kara Bautista", "Leo Mendoza"}

original_members = grade_7 | grade_8 | grade_9 | grade_10
master_set = original_members | set()

palette = ["#6366f1", "#ec4899", "#14b8a6", "#f59e0b", "#8b5cf6", "#3b82f6"]


def make_chip(name):
    initials = "".join(map(lambda word: word[0], name.split()))[:2].upper()
    color = palette[sum(map(ord, name)) % len(palette)]
    return (
        f'<div class="member-chip">'
        f'<span class="avatar" style="background:{color}">{initials}</span>'
        f'<span>{name}</span></div>'
    )


def make_welcome(name):
    return f'<div class="welcome">🎉 {name} joined the club!</div>'


def make_stat(label, value, extra_class=""):
    return (
        f'<div class="stat {extra_class}">'
        f'<div class="stat-value">{value}</div>'
        f'<div class="stat-label">{label}</div></div>'
    )


def result_checker(event=None):
    global master_set

    first = document.querySelector("#first_name").value
    last = document.querySelector("#last_name").value
    full_name = f"{first.strip()} {last.strip()}".strip().title()

    new_member = {full_name} - {""}
    just_added = new_member - master_set
    master_set = master_set | new_member
    added_later = master_set - original_members

    welcome_html = "".join(map(make_welcome, just_added))
    members_html = "".join(map(make_chip, sorted(master_set)))
    stats_html = "".join(
        [
            make_stat("Grade 7", len(grade_7)),
            make_stat("Grade 8", len(grade_8)),
            make_stat("Grade 9", len(grade_9)),
            make_stat("Grade 10", len(grade_10)),
            make_stat("New", len(added_later), "stat-new"),
        ]
    )

    document.querySelector("#output").innerHTML = f"""
        {welcome_html}
        <div class="stats">{stats_html}</div>
        <div class="results-title">All Club Members</div>
        <div class="members-wrap">{members_html}</div>
        <div class="total-box">
            <div class="total-number">{len(master_set)}</div>
            <div class="total-label">Total Number of Members</div>
        </div>
    """

    document.querySelector("#first_name").value = ""
    document.querySelector("#last_name").value = ""


result_checker()
