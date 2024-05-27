import customtkinter as ctk
import tkinter
from tkinter import messagebox

root = ctk.CTk()
root.title("Recon Dorking")
root.geometry("800x600")  # Set initial window size

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def show_info(button_text):
    messagebox.showinfo("Button Info", f"You clicked on: {button_text}")

header_frame = ctk.CTkFrame(root, height=50, corner_radius=10)
header_frame.pack(fill="x", padx=20, pady=10)

header_label = ctk.CTkLabel(header_frame, text="Recon Dorking Tool", font=("Arial", 24))
header_label.pack(pady=10)

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand=True, padx=20, pady=20)

prompt_label = ctk.CTkLabel(input_frame, text="Domain Name")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = ctk.CTkLabel(input_frame, text="Category")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = ctk.CTkComboBox(input_frame, values=["Search Engine", 
                                                      "Repositories", 
                                                      "Sub Domains", 
                                                      "Log Files" , 
                                                      "Web Files",
                                                      "Web Servers",
                                                      "Web Security",
                                                      "Miscellaneous"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

generate_button = ctk.CTkButton(input_frame, text="Search", command=lambda: show_info("Search"))
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10, ipadx=100)  # Set ipadx to widen the button

button_frame = ctk.CTkFrame(input_frame)
button_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Adding a matrix of buttons with different colors
button_texts = [
    ["Directory Listing", "Configuration Files", "Database Files", "WordPress", "Log Files", "Backup and Old Files", "Login Pages", "SQL Errors"],
    ["Apache Config Files", "Robots.txt File", "DomainEye", "Publicly Exposed Documents", "phpinfo0", "Finding Backdoors", "Install / Setup files", "Open Redirects"],
    ["Apache STRUTS RCE", "3rd Party Exposure", "Check Security Headers", "GitLab", "Find Pastebin entries", "Employees on LINKEDIN", ".htaccess sensitive files", "Find Subdomains"],
    ["Find Subdomains", "Find WordPress Sites", "Search in BitBucket and Atlassian", "PassiveTotal", "Search in Stackoverflow", "Search SWF in WayBack", "Search in GITHUB", "Search in OpenBugBounty"],
    ["Search in Reddit", "Test CrossDomain", "Check in ThreatCrowd", "git folder", "YouTube", "Digital Ocean Spaces", "Find .SWF file (Google)", "Find .SWF file (Yandex)"],
    ["Find WordPress Wayback Machine #1", "Search in WayBack Machine #2", "Search in WayBack Machine #3", "Reverse IP Lookup", "Traefik", "Cloud Storage and Buckets", "s3 Buckets", "Sourcecode - PublicWWW"],
    ["Check in CENSYS [IPV4]", "Check in CENSYS [DOMAINS]", "Check in CENSYS [CERTIFICATES]", "Search in SHODAN", "CVE-2020-0646 SharePoint RCE", "API Endpoints - WSDL", "Github GIST Searches", "Search in CT Logs"],
    ["Plaintext Password Leak", "What CMS?", "", "", "", "", "", ""]
]

button_colors = ["#CC4629", "#10511B", "#2745CC", "#CC2985"]

for row_idx, row in enumerate(button_texts):
    for col_idx, text in enumerate(row):
        if text:
            button = ctk.CTkButton(button_frame, text=text, fg_color=button_colors[col_idx % len(button_colors)], command=lambda t=text: show_info(t))
            button.grid(row=row_idx, column=col_idx, padx=10, pady=5)  # Adjust padding for better appearance

status_frame = ctk.CTkFrame(root, height=30, corner_radius=10)
status_frame.pack(fill="x", padx=20, pady=10)

status_label = ctk.CTkLabel(status_frame, text="Status: Ready", font=("Arial", 12))
status_label.pack(pady=5)

root.mainloop()
