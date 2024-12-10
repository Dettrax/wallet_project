# Create a management command to populate sample data
# wallet_app/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from wallet_app.models import Transaction, PhoneNumber, EmailAddress, BankAccount
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample users
        users = [
            ('john_doe', 'john@example.com', '123-45-6789'),
            ('jane_smith', 'jane@example.com', '987-65-4321'),
            ('bob_wilson', 'bob@example.com', '456-78-9123'),
        ]

        created_users = []
        for username, email, ssn in users:
            user = User.objects.create_user(
                username=username,
                email=email,
                password='dettrax23',
                ssn=ssn
            )
            created_users.append(user)

            # Add phone numbers
            PhoneNumber.objects.create(
                user=user,
                number=f'+1555{str(hash(username))[-7:]}',
                is_primary=True
            )

            # Add email addresses
            EmailAddress.objects.create(
                user=user,
                email=email,
                is_primary=True
            )

            # Add bank accounts
            BankAccount.objects.create(
                user=user,
                account_number=f'ACCT{str(hash(username))[-8:]}',
                routing_number='123456789',
                bank_name='Sample Bank',
                is_primary=True
            )

        # Create sample transactions
        transactions = [
            (created_users[0], created_users[1], 100.00, 'SEND'),
            (created_users[1], created_users[2], 50.00, 'SEND'),
            (created_users[2], created_users[0], 75.00, 'REQUEST'),
        ]

        for sender, receiver, amount, trans_type in transactions:
            Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=Decimal(str(amount)),
                transaction_type=trans_type,
                status='COMPLETED',
                description=f'Sample {trans_type.lower()} transaction'
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))