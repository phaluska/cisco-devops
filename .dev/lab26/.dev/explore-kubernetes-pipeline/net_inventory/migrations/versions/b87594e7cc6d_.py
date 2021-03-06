"""empty message

Revision ID: b87594e7cc6d
Revises: 
Create Date: 2019-02-07 15:07:44.413023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b87594e7cc6d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "device",
        sa.Column("hostname", sa.String(), nullable=False),
        sa.Column("tenant", sa.String(), nullable=True),
        sa.Column("ip_address", sa.String(), nullable=True),
        sa.Column("site", sa.String(), nullable=True),
        sa.Column("role", sa.String(), nullable=True),
        sa.Column("device_type", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("hostname"),
        sa.UniqueConstraint("ip_address"),
    )
    op.create_table(
        "permission",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("codename", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column("licensed", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("codename"),
        sa.UniqueConstraint("description"),
    )
    op.create_table(
        "user",
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("password", sa.String(length=100), nullable=True),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("username"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "user_role",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("short_name", sa.String(length=100), nullable=False),
        sa.Column("role_name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.Column("can_modify", sa.Boolean(), nullable=False),
        sa.Column("can_delete", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("role_name"),
        sa.UniqueConstraint("short_name"),
    )
    op.create_table(
        "permission_subscription",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("remote_role_id", sa.Integer(), nullable=False),
        sa.Column("remote_permission_id", sa.Integer(), nullable=False),
        sa.Column("state", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["remote_permission_id"], ["permission.id"]),
        sa.ForeignKeyConstraint(["remote_role_id"], ["user_role.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("remote_role_id", "remote_permission_id"),
    )
    op.create_table(
        "token",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("token", sa.String(length=100), nullable=False),
        sa.Column("expiration", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.username"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("token"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("token")
    op.drop_table("permission_subscription")
    op.drop_table("user_role")
    op.drop_table("user")
    op.drop_table("permission")
    op.drop_table("device")
    # ### end Alembic commands ###
