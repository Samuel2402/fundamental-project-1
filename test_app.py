from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Receipts, Store

#base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        #Create test registree
        mcdonalds = Store(name='mcdonalds', shop_address='63 Northbrook st', shop_postcode='rg14 1ae', takeaway=True)
        tesco = Store(name='tesco', shop_address='London rd, Newbury', shop_postcode='rg14 2bp', takeaway=False)
        coop = Store(name='coop', shop_address='Andover rd', shop_postcode='rg19 3bp', takeaway=False)
        
        #adding test receipts to db
        receipt1 = Receipts(most_expensive=5.09, cost_of_alcohol=0, receipt_total=11.36, takeaway=True, delivery_fee=1.99, delivery_time_mins=28, store_id=1, shop=mcdonalds)
        receipt2 = Receipts(most_expensive=2.80, cost_of_alcohol=16, receipt_total=11.90, store_id=2, shop=tesco)
        receipt3 = Receipts(most_expensive=3.00, cost_of_alcohol=0, receipt_total=18.76, store_id=2, shop=tesco)
        receipt4 = Receipts(most_expensive=2.00, cost_of_alcohol=0, receipt_total=20.91, store_id=2, shop=tesco)
        
        #Add and save to database
        store_list = [mcdonalds, tesco, coop]
        receipt_list = [receipt1, receipt2, receipt3, receipt4]
        for i in store_list:
            db.session.add(i)
        for i in receipt_list:
            db.session.add(i)
            db.session.commit()
        
    def teardown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

################################################## test read ##################################################################

class TestRead(TestBase):
    
    def test_read_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my website!', response.data)

    def test_read_receipt(self):
        response = self.client.get(url_for('read_receipts'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Read reciepts from database:', response.data)

    def test_read_stores(self):
        response = self.client.get(url_for('read_stores'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Read stores from database:', response.data)

    def test_resolve_receipt(self):
        response = self.client.get(url_for('resolve_receipt'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Edit reciept in database:', response.data)

    def test_add_receipt(self):
        response = self.client.get(url_for('add_receipt'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Reciept to database:', response.data)

    def test_delete_receipt(self):
        response = self.client.get(url_for('delete_receipt'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Remove reciepts from database:', response.data)

################################################## test add ##################################################################

class TestAdd(TestBase):

    def test_add_receipt(self):
        response = self.client.post(
            url_for('add_receipt'),
            data = dict(most_expensive=99, cost_of_alcohol=99, receipt_total=99, store_id=2),
            follow_redirects=True
        )
        self.assertIn(b'Receipt added!',response.data)

    def test_add_store(self):
        response = self.client.post(
            url_for('add_store'),
            data = dict(name='morrisons', shop_address='this rd, Newbury', shop_postcode='rg14 2xy', takeaway=True),
            follow_redirects=True
        )
        self.assertIn(b'',response.data)

################################################## test update ##################################################################

# class TestUpdate(TestBase):

#     def test_add_store(self):
#         response = self.client.post(
#             url_for('resolve_receipt'),
#             data = dict(id=1, most_expensive=most_expensive=99999999, cost_of_alcohol=99999999, receipt_total=99999999999, store_id=2, shop=tesco),
#             follow_redirects=True
#         )
#         self.assertIn(b'receipt updated',response.data)

    


    




