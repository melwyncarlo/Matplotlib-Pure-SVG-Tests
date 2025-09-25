import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

patches_list = (
    # (File name, Shape class, Positional arguments tuple, Keyword arguments dictionary)
    ('circle_1', plt.Circle, ((2.0, 0.0), 1.5), {'alpha': 0.5}),
    ('arc_1', patches.Arc, ((2.0, 0.0), 1, 1), {'linewidth': 2}),
    ('arc_2', patches.Arc, ((2.0, 0.0), 1, 1), {'theta2': 90}),
    ('arc_3', patches.Arc, ((2.0, 0.0), 1.5, 4.0), {'angle': -45, 'theta2': 180}),
    ('arc_4', patches.Arc, ((2.0, 0.0), 3.5, 1.5), {'theta1': 45, 'theta2': 135}),
    ('ellipse_1', patches.Ellipse, ((1.0, 1.0), 1.0, 3.0), {}),
    ('ellipse_2', patches.Ellipse, ((1.0, 1.0), 2.0, 1.0), {'angle':45}),
    ('annulus_1', patches.Annulus, ((2.0, 0.0), 1.5, 0.5, 45), {}),
    ('annulus_2', patches.Annulus, ((2.0, 0.0), (2.0, 1.0), 0.5, -45), {}),
    ('annulus_3', patches.Annulus, ((2.0, 0.0), 1.5, 0), {}),
    ('annulus_4', patches.Annulus, ((2.0, 0.0), 1.5, 1.5), {}),
    ('rectangle_1', plt.Rectangle, ((2.0, 0.0), 2.5, 1.5), {}),
    ('rectangle_2', plt.Rectangle, ((2.0, 0.0), 1.5, 2.5), {'angle': 45}),
    ('rectangle_3', plt.Rectangle, ((2.0, 0.0), 1.0, 1.0), {'angle': -45, 'rotation_point': 'center'}),
    ('wedge_1', patches.Wedge, ((2.0, 0.0), 1.5, 45, 90), {}),
    ('wedge_2', patches.Wedge, ((2.0, 0.0), 2.0, 45, 90), {'width': 1.5}),
    ('steppatch_1', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {}),
    ('steppatch_2', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {'orientation': 'horizontal'}),
    ('steppatch_3', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {'baseline': None}),
    ('steppatch_4', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {'baseline': None, 'fill': True}),
    ('steppatch_5', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {'baseline': 0.5}),
    ('steppatch_6', patches.StepPatch, ([1, 2, 3, 2, 1], range(1, 7)), {'baseline': [0, 0.5, 0, 0.5, 0]}),
    ('polygon_1', plt.Polygon, ([[1, 1], [1, 2], [2, 2], [2, 4], [3, 0]],), {}),
    ('polygon_2', plt.Polygon, ([[1, 1], [1, 2], [2, 2], [2, 4], [3, 0]],), {'closed': False}),
    ('regularpolygon_1', patches.RegularPolygon, ((2.0, 0.0), 3), {}),
    ('regularpolygon_2', patches.RegularPolygon, ((2.0, 0.0), 5), {}),
    ('regularpolygon_3', patches.RegularPolygon, ((2.0, 0.0), 10), {}),
    ('circlepolygon_1', patches.CirclePolygon, ((2.0, 0.0),), {}),
    ('arrow_1', plt.Arrow, (2.0, 0.0, 5, 2), {}),
    ('arrow_2', plt.Arrow, (2.0, 0.0, 5, 2), {'width': 2}),
    ('fancyarrow_1', patches.FancyArrow, (2, 0, 5, 2), {}),
    ('fancyarrow_2', patches.FancyArrow, (2, 0, 5, 2), {'width': 2}),
    ('shadow_1', patches.Shadow, (1.0, -1.0), {}),
)

if os.path.isdir('images'):
    for file in os.listdir('images'):
        os.remove('images/' + file)
else:
    os.mkdir('images')

max_num_len = len(str(len(patches_list)))
max_str_len = len(max([elem[0] for elem in patches_list], key=len))

print('\n Testing:\n')

i = 0
for patch_data in patches_list:
    file_paths = []
    for pure_svg_mode in [False, True]:
        i += 1
        print(f' {str(i).rjust(max_num_len)}. {patch_data[0].ljust(max_str_len)} ::  {'Pure SVG' if pure_svg_mode else (' ' * 9) + 'Original'}', end=(' ' if pure_svg_mode else None), flush=True)
        with open('pure_svg_mode', 'w') as f:
            f.write(str(int(pure_svg_mode)))
        plt.close()
        if patch_data[0].startswith('shadow'):
            main_patch = plt.Rectangle((0, 0), 5, 3)
            plt.gca().add_patch(main_patch)
            plt.gca().add_patch(patch_data[1](main_patch, *patch_data[2], **patch_data[3]))
        else:
            plt.gca().add_patch(patch_data[1](*patch_data[2], **patch_data[3]))
        plt.autoscale()
        plt.gca().set_aspect('equal')
        plt.gca().set_axis_off()
        file_paths.append('images/' + patch_data[0] + ('_pure_svg' if pure_svg_mode else '_original') + '.svg')
        plt.savefig(file_paths[-1])
    plt.savefig('images/' + patch_data[0] + '.png', dpi=72)
    print((' ' * 9) + f'[Diff = {str(os.path.getsize(file_paths[1]) - os.path.getsize(file_paths[0])).rjust(4)} B]')
