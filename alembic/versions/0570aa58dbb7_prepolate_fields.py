"""prepolate fields

Revision ID: 0570aa58dbb7
Revises: 3f8aceec8ca2
Create Date: 2025-01-24 21:07:31.248157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '0570aa58dbb7'
down_revision: Union[str, None] = '3f8aceec8ca2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    con = op.get_bind()
    con.execute(text("""
                INSERT INTO activity (name, parent_id)
            VALUES
                ('Corporate', NULL),
                ('Technology', 1),
                ('Healthcare', 1),
                ('Software Development', 2),
                ('Hardware Development', 2),
                ('Medical Devices', 3),
                ('Pharmaceutical Research', 3),
                ('Web Development', 4),
                ('Mobile Applications', 4),
                ('Cloud Computing', 4);
            
            INSERT INTO building (address, location)
            VALUES
                ('789 Pine Road, Springfield', 'SRID=4326;POINT(41.8781 -87.6298)'),
                ('321 Oak Street, Gotham', 'SRID=4326;POINT(34.0522 -118.2437)'),
                ('654 Elm Avenue, Star City', 'SRID=4326;POINT(37.7749 -122.4194)'),
                ('987 Birch Blvd, Coast City', 'SRID=4326;POINT(29.7604 -95.3698)'),
                ('159 Cedar Lane, Central City', 'SRID=4326;POINT(47.6062 -122.3321)'),
                ('753 Willow Way, Blüdhaven', 'SRID=4326;POINT(42.3601 -71.0589)'),
                ('852 Aspen Court, Keystone', 'SRID=4326;POINT(38.9072 -77.0369)'),
                ('951 Redwood Drive, Fawcett City', 'SRID=4326;POINT(40.4406 -79.9959)'),
                ('159 Sequoia Street, National City', 'SRID=4326;POINT(33.7488 -84.3880)'),
                ('456 Magnolia Avenue, Smallville', 'SRID=4326;POINT(36.1627 -86.7816)');
            
            INSERT INTO organization (name, building_id)
            VALUES
                ('Digital Future', 3),
                ('GreenTech Solutions', 4),
                ('Quantum Health', 5),
                ('Bright Ideas Co.', 6),
                ('NextGen Innovations', 7),
                ('EcoEnergy Inc.', 8),
                ('MedTech Pro', 9),
                ('Global Solutions', 10),
                ('Tech Nexus', 1),
                ('AI Pioneers', 2);
            
            INSERT INTO organization_phones (organization_id, phone_number)
            VALUES
                (4, '111-222-3333'),
                (5, '222-333-4444'),
                (6, '333-444-5555'),
                (7, '444-555-6666'),
                (8, '555-666-7777'),
                (9, '666-777-8888'),
                (10, '777-888-9999'),
                (1, '888-999-0000'),
                (2, '999-000-1111'),
                (3, '000-111-2222');
            
            INSERT INTO organization_activity (organization_id, activity_id)
            VALUES
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 10),
                (10, 4),
                (1, 2),
                (2, 3),
                (3, 1);
    """))


def downgrade() -> None:
    con = op.get_bind()
    con.execute(
        text(
            """
        DELETE FROM organization_activity;

        DELETE FROM organization_phones;
        
        DELETE FROM organization;

        DELETE FROM building;

        DELETE FROM activity;"""
        )
    )
