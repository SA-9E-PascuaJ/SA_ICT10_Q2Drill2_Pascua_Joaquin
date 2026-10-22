from pyscript import document

grade_7 = {"Ana Santos", "Ben Reyes", "Carla Lim"}
grade_8 = {"Dario Cruz", "Elena Tan", "Felix Go"}
grade_9 = {"Gina Diaz", "Hugo Ramos", "Isabel Co"}
grade_10 = {"Jared Uy", "Kara Bautista", "Leo Mendoza"}

master_set = grade_7 | grade_8 | grade_9 | grade_10


def result_checker(event=None):
    global master_set

    first = document.querySelector("#first_name").value
    last = document.querySelector("#last_name").value
    full_name = f"{first.strip()} {last.strip()}".strip().title()

    new_member = {full_name} - {""}
    master_set = master_set | new_member

    members_html = "<br>".join(sorted(master_set))
    document.querySelector("#output").innerHTML = f"""
        <strong>All Club Members:</strong><br>
        {members_html}
        <br><br>
        <strong>Total Number of Members:</strong> {len(master_set)}
    """

    document.querySelector("#first_name").value = ""
    document.querySelector("#last_name").value = ""


result_checker()
