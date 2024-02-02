"""empty message

Revision ID: ba4478a04207
Revises: ebdc83a62dea
Create Date: 2024-02-02 18:52:50.650333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba4478a04207'
down_revision = 'ebdc83a62dea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_user', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_people', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_vehicles', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_species', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_planets', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['id_planets'], ['id'])
        batch_op.create_foreign_key(None, 'people', ['id_people'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['id_user'], ['id'])
        batch_op.create_foreign_key(None, 'species', ['id_species'], ['id'])
        batch_op.create_foreign_key(None, 'vehicles', ['id_vehicles'], ['id'])

    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.alter_column('opening_crawl',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('director',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('producer',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('release_date',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('hair_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('height',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('mass',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('skin_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('diameter',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('rotation_period',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('orbital_period',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('gravity',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('population',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('surface_water',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.alter_column('classification',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('designation',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('average_height',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('average_lifespan',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('eye_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('hair_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('skin_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('language',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('starship_class',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('manufacturer',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('cost_in_credits',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('length',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('crew',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('passengers',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('max_atmosphering_speed',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('hyperdrive_rating',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('MGLT',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('cargo_capacity',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('consumables',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('vehicle_class',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('manufacturer',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('length',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('cost_in_credits',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('crew',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('passengers',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('max_atmosphering_speed',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('cargo_capacity',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('consumables',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('consumables',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('cargo_capacity',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('max_atmosphering_speed',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('passengers',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('crew',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('cost_in_credits',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('length',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('manufacturer',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('vehicle_class',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('consumables',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('cargo_capacity',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('MGLT',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('hyperdrive_rating',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('max_atmosphering_speed',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('passengers',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('crew',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('length',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('cost_in_credits',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('manufacturer',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('starship_class',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('language',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('skin_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('hair_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('eye_colors',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('average_lifespan',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('average_height',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('designation',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('classification',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('surface_water',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('population',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('gravity',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('orbital_period',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('rotation_period',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('diameter',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('skin_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('mass',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('height',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('hair_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.alter_column('edited',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('release_date',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('producer',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('director',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('opening_crawl',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)

    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_planets')
        batch_op.drop_column('id_species')
        batch_op.drop_column('id_vehicles')
        batch_op.drop_column('id_people')
        batch_op.drop_column('id_user')

    # ### end Alembic commands ###
