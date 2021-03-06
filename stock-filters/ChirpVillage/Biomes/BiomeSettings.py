from BlockTypes import blocks
# biome names come from biome_types.py
# material names are currently hardcoded
# block id's can be found at https://minecraft-ids.grahamedgecombe.com/
biomeSettings = {
    "Plains": { # Default
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Cobblestone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Oak Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    },
    "Desert": {
        "wall": blocks['Chiseled Sandstone'], 
        "fence": blocks['Acacia Fence'],
        "floor": blocks['Sandstone'],
        "road": blocks['Smooth Sandstone'],
        "door": blocks['Air'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Smooth Sandstone'],
        'hedge': blocks['Cactus'],
        'roof': blocks['Sandstone'],
        'crop': blocks['Cactus'],
        'soil': blocks['Sand'],
        'bridge': blocks['Chiseled Sandstone']
    },
    "Forest": {
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Stone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Oak Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    },
    "Jungle": {
        "wall": blocks['Jungle Wood Planks'],
        "fence": blocks['Jungle Fence'],
        "floor": blocks['Moss Stone'],
        "road": blocks['Moss Stone'],
        "door": blocks['Jungle Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Jungle Wood'],
        'hedge': blocks['Jungle Leaves'],
        'roof': blocks['Mossy Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Jungle Wood Planks']
    },
    "Taiga": {
        "wall": blocks['Spruce Wood Planks'],
        "fence": blocks['Spruce Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Chiseled Stone Bricks'],
        "door": blocks['Spruce Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Spruce Wood'],
        'hedge': blocks['Spruce Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Potatoes'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Spruce Wood Planks']
    },
    "Swamp": {
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Moss Stone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Oak Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Potatoes'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    },
    "Birch Forest": {
        "wall": blocks['Birch Wood Planks'],
        "fence": blocks['Birch Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Stone Bricks'],
        "door": blocks['Birch Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Birch Wood'],
        'hedge': blocks['Birch Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Carrots'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Birch Wood Planks']
    },
    "Dark Forest": {
        "wall": blocks['Dark Oak Wood Planks'],
        "fence": blocks['Dark Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Stone'],
        "door": blocks['Dark Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Dark Oak Wood'],
        'hedge': blocks['Dark Oak Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Dark Oak Wood Planks']
    },
    "River Beach": {
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Stone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Sugar Cane'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Sugar Cane'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    },
    "Ice": {
        "wall": blocks['Quartz Block'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Chiseled Quartz Block'],
        "road": blocks['Moss Stone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Piller Quartz Block'],
        'hedge': blocks['Snow Block'],
        'roof': blocks['Quartz Block'],
        'crop': blocks['Potatoes'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Piller Quartz Block']
    },
    "Mountains": {
        "wall": blocks['Bricks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Stone Bricks'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Oak Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Mossy Stone Bricks']
    },
    "Mushroom": {
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Polished Granite'],
        "road": blocks['Moss Stone'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Red Stained Glass Pane'],
        "beam": blocks['Hardened Clay'],
        'hedge': blocks['Red Mushroom'],
        'roof': blocks['Polished Granite'],
        'crop': blocks['Red Mushroom'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    },
	"Savanna": {
        "wall": blocks['Acacia Wood Planks'],
        "fence": blocks['Acacia Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Mossy Stone Bricks'],
        "door": blocks['Acacia Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Acacia Wood'],
        'hedge': blocks['Acacia Leaves'],
        'roof': blocks['Stone Bricks'],
        'crop': blocks['Wheat'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Acacia Wood Planks']
    },
    "Badlands": {
        "wall": blocks['White Glazed Terracotta'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Gray Glazed Terracotta'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Black Glazed Terracotta'],
        'hedge': blocks['Cactus'],
        'roof': blocks['Gray Glazed Terracotta'],
        'crop': blocks['Cactus'],
        'soil': blocks['Red Sand'],
        'bridge': blocks['Yellow Glazed Terracotta']
    },
    "Aquatic": {
        "wall": blocks['Oak Wood Planks'],
        "fence": blocks['Oak Fence'],
        "floor": blocks['Stone Bricks'],
        "road": blocks['Mossy Stone Bricks'],
        "door": blocks['Oak Door Block'],
        'window': blocks['Glass Pane'],
        "beam": blocks['Oak Wood'],
        'hedge': blocks['Oak Leaves'],
        'roof': blocks['Mossy Stone Bricks'],
        'crop': blocks['Sugar Cane'],
        'soil': blocks['Farmland'],
        'bridge': blocks['Oak Wood Planks']
    }
}
