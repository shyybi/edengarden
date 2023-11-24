def map():
    from pytmx.util_pygame import load_pygame
    import pygame
    class Tile(pygame.sprite.Sprite):
        def __init__(self,pos,surf,groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_rect(topleft = pos)

    tmx_data = load_pygame('./tiledmap/Tiles/City/test_debug.tmx')
    sprite_group = pygame.sprite.Group()

    for layer in tmx_data.visible_layers:
        if hasattr(layer, 'data'):
            for x,y,surf in layer.tiles():
                pos = (x * 1240, y * 1240)
                Tile(pos = pos, surf = surf, groups = sprite_group)
