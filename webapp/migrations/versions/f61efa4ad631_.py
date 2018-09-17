"""empty message

Revision ID: f61efa4ad631
Revises: 6088faf1ccd5
Create Date: 2018-09-14 13:43:44.315918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f61efa4ad631'
down_revision = '6088faf1ccd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assignments_problems',
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignments.id'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['problems.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments_problems')
    op.drop_table('assignments')
    # ### end Alembic commands ###
