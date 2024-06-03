import tkinter as tk

def calc_dc():
    dbP = float(entry_dbP.get())
    dbABS = float(entry_dbABS.get())
    dbCOXA = float(entry_dbCOXA.get())
    dbTRICEPS = float(entry_dbTRICEPS.get())
    dbSUBESCAPULAR = float(entry_dbSUBESCAPULAR.get())
    dbSUPRAILIACA = float(entry_dbSUPRAILIACA.get())
    dbAXILAR = float(entry_dbAXILAR.get())
    idade = float(entry_idade.get())

    somatorio = dbP + dbABS + dbCOXA + dbTRICEPS + dbSUBESCAPULAR + dbSUPRAILIACA + dbAXILAR

    Dc = 1.1120 - (0.00043499 * somatorio) + (0.00000055 * (somatorio ** 2)) + (0.00028826 * idade)
    return Dc

def calc_gordura_corporal():
    dc = calc_dc()
    gc1 = ((4.95 / dc) - 4.50) * 100
    gc2 = ((4.57 / dc) - 4.142) * 100
    resultado_label.config(text=f'GC1: {gc1:.2f}%, GC2: {gc2:.2f}%')

# Configurações da janela principal
root = tk.Tk()
root.title("Calculadora de Porcentagem de Gordura Corporal")

# Widgets
label_dbP = tk.Label(root, text="dbP:")
label_dbP.grid(row=0, column=0)
entry_dbP = tk.Entry(root)
entry_dbP.grid(row=0, column=1)

label_dbABS = tk.Label(root, text="dbABS:")
label_dbABS.grid(row=1, column=0)
entry_dbABS = tk.Entry(root)
entry_dbABS.grid(row=1, column=1)

label_dbCOXA = tk.Label(root, text="dbCOXA:")
label_dbCOXA.grid(row=2, column=0)
entry_dbCOXA = tk.Entry(root)
entry_dbCOXA.grid(row=2, column=1)

label_dbTRICEPS = tk.Label(root, text="dbTRICEPS:")
label_dbTRICEPS.grid(row=3, column=0)
entry_dbTRICEPS = tk.Entry(root)
entry_dbTRICEPS.grid(row=3, column=1)

label_dbSUBESCAPULAR = tk.Label(root, text="dbSUBESCAPULAR:")
label_dbSUBESCAPULAR.grid(row=4, column=0)
entry_dbSUBESCAPULAR = tk.Entry(root)
entry_dbSUBESCAPULAR.grid(row=4, column=1)

label_dbSUPRAILIACA = tk.Label(root, text="dbSUPRAILIACA:")
label_dbSUPRAILIACA.grid(row=5, column=0)
entry_dbSUPRAILIACA = tk.Entry(root)
entry_dbSUPRAILIACA.grid(row=5, column=1)

label_dbAXILAR = tk.Label(root, text="dbAXILAR:")
label_dbAXILAR.grid(row=6, column=0)
entry_dbAXILAR = tk.Entry(root)
entry_dbAXILAR.grid(row=6, column=1)

label_idade = tk.Label(root, text="Digite sua idade:")
label_idade.grid(row=7, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=7, column=1)

calcular_button = tk.Button(root, text="Calcular", command=calc_gordura_corporal)
calcular_button.grid(row=8, columnspan=2)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=9, columnspan=2)

# Executar a aplicação
root.mainloop()
