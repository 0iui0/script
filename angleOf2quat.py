import numpy as np

def quaternion_angle(q1, q2):
    # Normalize the quaternions
    q1 = q1 / np.linalg.norm(q1)
    q2 = q2 / np.linalg.norm(q2)

    # Calculate the dot product of the quaternions
    dot_product = np.dot(q1, q2)

    # Calculate the angle between the quaternions
    angle = 2 * np.arccos(np.abs(dot_product))

    # Convert quaternions to 3-dimensional vectors
    v1 = q1[:-1]
    v2 = q2[:-1]

    # Calculate the axis of the angle
    cross_product = np.cross(v1, v2)
    axis = cross_product / np.linalg.norm(cross_product)

    return angle, axis

# Example data
q1 = np.array([0.9991220967818202, -0.005944648789690513, 0.006944363164188716, 0.040883648238755524])
q2 = np.array([-0.7024043107671893, 0.7107256381936788, -0.030077658614088048, -0.024343086947879455])

# Calculate the angle and axis between the quaternions
angle, axis = quaternion_angle(q1, q2)

print("Angle between the quaternions:", np.degrees(angle), "degrees")
print("Axis of the angle:", axis)
