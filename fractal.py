# Importing standard python libraries
import random
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# Importing standard Qiskit libraries
from qiskit import *
from qiskit.visualization import plot_state_qsphere
from qiskit_aer import *
from PIL import  Image

def randomize_circuit(circuit):
    # Losowe kąty dla bramki U
    theta = random.uniform(0, 2*pi)
    phi = random.uniform(0, 2*pi)
    lam = random.uniform(0, 2*pi)

    # Zastosuj bramkę U z losowymi kątami do drugiego kubitu
    circuit.u(theta, phi, lam, 1)

    return circuit

# Start with a 2-qubit quantum circuit (Bell state + a rotation) yielding a nice fractal. Change the circuit as you like.
circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
circuit = randomize_circuit(circuit)
editor2 = circuit


# View the circiut quantum state on the qshere
qc2 = circuit
plot_state_qsphere(qc2)

# Run the circuit with the state vector simulator
qc2 = circuit
backend = Aer.get_backend('statevector_simulator')

# Use the `run` method instead of `execute`
job = backend.run(qc2)

# Get the result
result = job.result()

# Get the statevector
out = result.get_statevector()

# print(out)
plot_state_qsphere(out)
# Obtain the four complex amplitudes from the state vector
a00 = out.data[0]
a01 = out.data[1]
a10 = out.data[2]
a11 = out.data[3]

# Goal: One complex number for the Julia set fractal.
# Divide a00 with a11 - which may indicate entanglement.
if a11.real != 0 or a11.imag != 0:
    z1 = a00 / a11
    z1 = round(z1.real, 2) + round(z1.imag, 2) * 1j
else:
    z1 = 0

# Divide a01 with a10.
if a10.real != 0 or a10.imag != 0:
    z2 = a01 / a10
    z2 = round(z2.real, 2) + round(z2.imag, 2) * 1j
else:
    z2 = 0

# Obtain the complex number for the Julia set fractal.
if z2.real != 0 or z2.imag != 0:
    z = z1 / z2  # (z1+z2)/2
    z = round(z.real, 2) + round(z.imag, 2) * 1j
else:
    z = 0

print("z = ", z)

# Define the size
size = 1000
heightsize = size
widthsize = size


def julia_set(c=z, height=heightsize, width=widthsize, x=0, y=0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5 * height / width
    x_from = x - x_width / zoom
    x_to = x + x_width / zoom
    y_from = y - y_height / zoom
    y_to = y + y_height / zoom

    # Here the actual algorithm starts and the z paramter is defined for the Julia set function
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y

    # Initialize c to the complex number obtained from the quantum circuit
    c = np.full(z.shape, c)

    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m] ** 2 + c[m]
        m[np.abs(z) > 2] = False
        div_time[m] = i
    return div_time

# plot the Julia set fractal
plt.figure(dpi=300)  # Ustawiamy rozdzielczość na 300 DPI, co odpowiada wymiarom w pikselach
plt.axis('off')
# Definicja własnej mapy kolorów
colors = [ '#3d499d', '#3b44a4', '#3940aa', '#373cb1', '#3537b8', '#3332bf', '#312ec6', '#2f29cc', '#2d24d3', '#2b20da',
    '#291be1', '#2717e7', '#2512ee', '#230df5', '#2108fc', '#1f1a37', '#364e60', '#4c847f', '#62ba9f', '#78f0bf',
    '#8cffd0', '#a2ffd9', '#b6ffe2', '#caffeb', '#dbe7bd', '#f1f5dd', '#f7f9e2', '#fcfbe6', '#ffffeb', '#ffffcf',
    '#ffffb3', '#ffff97', '#ffff7b', '#ffff5f', '#ffff43', '#ffff27', '#ffff0b', '#f7ed00', '#ebdb00', '#dfc400'
]
cmap_custom = ListedColormap(colors)
aspect_ratio = widthsize / heightsize
plt.imshow(julia_set(), cmap=cmap_custom, extent=[-aspect_ratio/2, aspect_ratio/2, -0.5, 0.5], aspect=aspect_ratio)
plt.savefig('fractal.png', bbox_inches='tight', pad_inches=0, transparent=True)
plt.show(block=True)

image1 = Image.open("fractal.png")
image2 = Image.open("gogh_night.png")

nowy_rozmiar = (int(image1.width // 1.6), image1.height // 2)

# Zmniejsz obraz
image1 = image1.resize(nowy_rozmiar)

# Check the sizes of the images
width1, height1 = image1.size
width2, height2 = image2.size

# Create a new image with an alpha channel
new_image = Image.new("RGBA", (width2, height2+100))

# Paste image1 onto the new image at (0,0)
new_image.paste(image1, (0, 0))

# Paste image2 onto the new image at (0, height1), using the transparency mask of image2
new_image.paste(image2, (0, 100), image2)

# Save the new image
new_image.save("new_image.png")