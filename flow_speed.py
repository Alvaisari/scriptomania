# estimate the aerosol flow speeds in tubing sections of different width

# libraries
import numpy as np
import matplotlib.pyplot as plt


# functions
def flow_speed(d_tube, flow):
    # d_tube: inner diameter of a tube in mm
    # flow: [l/min]
    # return flow speed [m/s]
    return flow * 1e-3 / (3600 * np.pi * (d_tube * 1e-3)**2 / 4)


# correspondence of outer and inner diameters of silicone tubes
tubes = {
    '1/4"': 3.175,  # 6.35 mm outer
    '8 mm': 5,
    '5/8"': 12.7,  # 15.875 mm outer
    '19 mm': 14
}

# flow, l/min
flow = np.arange(0.3, 30, 0.1)

# flow speed for each tube
v_flow = {}
for tube in tubes:
    v_flow[tube] = []
    for i in flow:
        v_flow[tube].append(flow_speed(tubes[tube],
                                       i))

legend = []  # add outer diameters here for plotting
fig, ax = plt.subplots(figsize=(10, 6))  # plot size

# plot figures
for tube in v_flow:
    ax.plot(flow,
            v_flow[tube])
    legend.append(tube)

# design figures
plt.xlim(0, flow[-1] + 1)
plt.xlabel('Volumetric flow rate [l/min]')
plt.ylabel('Flow velocity [m/s]')
plt.legend(legend)
plt.grid(True)

plt.show()

# save plot
plt.savefig('Flow velocity all.jpg')
