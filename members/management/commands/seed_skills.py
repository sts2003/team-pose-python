from django.core.management.base import BaseCommand
from django_seed import Seed
from members import models as members_model


class Command(BaseCommand):
    help = "🐳 This Command is Create Many Skills 🐳"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=2, help="How many want to create Skills?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            members_model.SkillModel,
            number,
            {
                "skill_name": lambda x: seeder.faker.name(),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Create Skill !!!"))
