import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe


os.makedirs("images", exist_ok=True)


# ---------- Style ----------

FIG_W = 16
FIG_H = 9

BOX_W = 2.5
BOX_H = 0.9

BOX_COLOR = "#EAF4FF"
EDGE_COLOR = "#1565C0"
TITLE_COLOR = "#0D47A1"
TEXT_COLOR = "#212121"
ARROW_COLOR = "#455A64"


# ---------- Helper Functions ----------

def create_canvas(title):

    fig, ax = plt.subplots(
        figsize=(FIG_W, FIG_H)
    )

    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)

    ax.axis("off")


    ax.set_title(
        title,
        fontsize=22,
        fontweight="bold",
        color=TITLE_COLOR,
        pad=20
    )


    return fig, ax



def draw_box(ax, x, y, text):

    box = FancyBboxPatch(
        (x, y),
        BOX_W,
        BOX_H,
        boxstyle="round,pad=0.08",
        linewidth=2,
        edgecolor=EDGE_COLOR,
        facecolor=BOX_COLOR
    )


    box.set_path_effects(
        [
            pe.SimplePatchShadow(
                offset=(2,-2),
                alpha=0.3
            ),
            pe.Normal()
        ]
    )


    ax.add_patch(box)


    ax.text(
        x + BOX_W/2,
        y + BOX_H/2,
        text,
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color=TEXT_COLOR
    )



def draw_arrow(ax,x1,y1,x2,y2):

    arrow = FancyArrowPatch(
        (x1,y1),
        (x2,y2),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=2,
        color=ARROW_COLOR
    )

    ax.add_patch(arrow)



def save(fig,name):

    plt.savefig(
        "images/" + name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()



# ==================================================
# 1. SYSTEM ARCHITECTURE
# ==================================================

def system_architecture():

    fig,ax=create_canvas(
        "Java Chat App - System Architecture"
    )


    draw_box(ax,1,8,"Client 1")
    draw_box(ax,7.7,8,"Client 2")
    draw_box(ax,14,8,"Client 3")


    draw_box(ax,7.7,5,"Chat Server")


    draw_box(ax,7.7,2,"Chat Logger")


    draw_arrow(ax,2.2,8,8.5,5.9)
    draw_arrow(ax,8.9,8,8.9,5.9)
    draw_arrow(ax,15.2,8,9.6,5.9)


    draw_arrow(ax,9,5,9,2.9)



    ax.text(
        9,
        9.3,
        "Multiple clients connect using TCP sockets",
        ha="center",
        fontsize=13,
        fontweight="bold"
    )


    save(
        fig,
        "system_architecture.png"
    )



# ==================================================
# 2. CLIENT SERVER FLOW
# ==================================================

def client_server_flow():

    fig,ax=create_canvas(
        "Client Server Communication Flow"
    )


    draw_box(ax,1,5,"Client")
    draw_box(ax,7.7,5,"Java Server")
    draw_box(ax,14,5,"Client")


    draw_arrow(
        ax,
        3.5,
        5.45,
        7.7,
        5.45
    )


    draw_arrow(
        ax,
        10.2,
        5.45,
        14,
        5.45
    )


    ax.text(
        9,
        8.2,
        "TCP Socket Communication",
        ha="center",
        fontsize=14,
        fontweight="bold"
    )


    save(
        fig,
        "client_server_flow.png"
    )



# ==================================================
# 3. THREAD WORKFLOW
# ==================================================

def thread_workflow():

    fig,ax=create_canvas(
        "Multithreaded Server Workflow"
    )


    draw_box(ax,7.7,8,"Server")

    draw_box(ax,7.7,6,"Accept Client")


    draw_box(ax,1,3.5,"Client Thread 1")
    draw_box(ax,7.7,3.5,"Client Thread 2")
    draw_box(ax,14,3.5,"Client Thread 3")


    draw_box(ax,7.7,1,"Message Handling")


    draw_arrow(ax,9,8,9,6.9)


    draw_arrow(ax,8.5,6,2.5,4.4)
    draw_arrow(ax,9,6,9,4.4)
    draw_arrow(ax,9.5,6,15,4.4)


    draw_arrow(ax,2.5,3.5,8.5,1.9)
    draw_arrow(ax,9,3.5,9,1.9)
    draw_arrow(ax,15,3.5,9.5,1.9)


    save(
        fig,
        "thread_workflow.png"
    )
# ==================================================
# 4. MESSAGE FLOW
# ==================================================

def message_flow():

    fig, ax = create_canvas(
        "Chat Message Flow"
    )


    draw_box(ax,1,7.5,"User A")

    draw_box(ax,7.7,7.5,"Chat Server")

    draw_box(ax,14,7.5,"User B")


    draw_box(ax,14,4,"User C")


    draw_box(ax,7.7,1,"Chat Logger")



    # User A -> Server
    draw_arrow(
        ax,
        3.5,
        7.95,
        7.7,
        7.95
    )


    # Server -> User B
    draw_arrow(
        ax,
        10.2,
        7.95,
        14,
        7.95
    )


    # Server -> User C
    draw_arrow(
        ax,
        10.2,
        7.7,
        14,
        4.5
    )


    # Server -> Logger
    draw_arrow(
        ax,
        9,
        7.5,
        9,
        1.9
    )



    ax.text(
        9,
        9.3,
        "Server receives and routes messages",
        ha="center",
        fontsize=14,
        fontweight="bold"
    )


    save(
        fig,
        "message_flow.png"
    )



# ==================================================
# 5. COMPLETE PROJECT WORKFLOW
# ==================================================

def project_workflow():

    fig, ax = create_canvas(
        "Complete Java Chat Application Workflow"
    )


    # Top flow

    draw_box(ax,0.8,7.8,"Start\nServer")

    draw_box(ax,4,7.8,"Client\nConnect")

    draw_box(ax,7.2,7.8,"Enter\nUsername")

    draw_box(ax,10.4,7.8,"Create\nThread")

    draw_box(ax,13.6,7.8,"Join\nChat")



    # Bottom flow

    draw_box(ax,0.8,3.3,"Send\nMessage")

    draw_box(ax,4,3.3,"Server\nReceives")

    draw_box(ax,7.2,3.3,"Process\nMessage")

    draw_box(ax,10.4,3.3,"Broadcast")

    draw_box(ax,13.6,3.3,"Receive\nMessage")



    # Logger

    draw_box(ax,7.2,0.8,"Save\nChat Log")



    # Top arrows

    draw_arrow(ax,3.3,8.25,4,8.25)

    draw_arrow(ax,6.5,8.25,7.2,8.25)

    draw_arrow(ax,9.7,8.25,10.4,8.25)

    draw_arrow(ax,12.9,8.25,13.6,8.25)



    # Down

    draw_arrow(
        ax,
        14.8,
        7.8,
        14.8,
        4.3
    )



    # Bottom arrows

    draw_arrow(ax,13.6,3.75,12.9,3.75)

    draw_arrow(ax,10.4,3.75,9.7,3.75)

    draw_arrow(ax,7.2,3.75,6.5,3.75)

    draw_arrow(ax,4,3.75,3.3,3.75)



    # Logger arrow

    draw_arrow(
        ax,
        8.5,
        3.3,
        8.5,
        1.7
    )



    save(
        fig,
        "project_workflow.png"
    )



# ==================================================
# MAIN FUNCTION
# ==================================================

def main():

    print("="*50)

    print(
        "Generating Java Chat App Diagrams..."
    )

    print("="*50)


    system_architecture()

    client_server_flow()

    thread_workflow()

    message_flow()

    project_workflow()



    print(
        "✔ system_architecture.png"
    )

    print(
        "✔ client_server_flow.png"
    )

    print(
        "✔ thread_workflow.png"
    )

    print(
        "✔ message_flow.png"
    )

    print(
        "✔ project_workflow.png"
    )


    print(
        "\nAll images generated inside images folder."
    )



if __name__ == "__main__":

    main()