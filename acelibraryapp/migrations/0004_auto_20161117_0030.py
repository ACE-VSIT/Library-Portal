# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 19:00
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('acelibraryapp', '0003_auto_20161117_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(43, 'AAyush Gupta'), (9, 'Aarti Narang'), (60, 'AdiTya Raman'), (148, 'Aditi Mishra'), (72, 'Aditya Agrawal'), (1, 'Aditya Dhawan'), (71, 'Afzal Ahmed'), (86, 'Ajay Mahor'), (11, 'Akshay Dureja'), (131, 'Akshay Katyal'), (75, 'Akshita Gupta'), (126, 'Amritasha Chhabra'), (105, 'Ankit Tayal'), (106, 'Ankit Tayal'), (116, 'Anmol Gro Ver'), (12, 'Anshul Bansal'), (46, 'Anukriti Gupta'), (53, 'Anurag Panwar'), (141, 'Apram Lamba'), (22, 'Arihant Jain'), (85, 'Arjun'), (104, 'Arpan Gupta'), (137, 'Arsh Saxena'), (2, 'Ashish Pahwa'), (140, 'Ashu Jaiswal'), (52, 'Ashu R. Kumar'), (42, 'Ashutosh Upadhyay'), (89, 'Avi Dhawan'), (41, 'Ayush Gupta'), (138, 'Ayushi Gupta'), (30, 'Bhavay Khanna'), (112, 'Charvi Wadhwa'), (91, 'Chirag Dudheria'), (8, 'Debjeet Majumdar'), (25, 'Deepanshu Gupta'), (3, 'Desmond Miles'), (62, 'Devansh Gupta'), (38, 'Devender Raghav'), (35, 'Dhruv Goel'), (92, 'Dhruv Shah'), (118, 'Dhruv Shah'), (101, 'Gaurav Gogia'), (87, 'Gaurav Saini'), (94, 'Gaurav Taneja'), (54, 'Gursimrat Singh'), (45, 'Harsh Vasudeva'), (93, 'Harshit Garg'), (28, 'Harshit Jain'), (29, 'Harshit Jain'), (67, 'Himanshu Chauhan'), (23, 'Himanshu Dua'), (130, 'Jaskirat Singh'), (59, 'Jobin Sabu'), (102, 'Kanav Kumar'), (115, 'Kandarp Gautam'), (64, 'Kaps Gera'), (95, 'Kartik Ahuja'), (76, 'Kartik Gupta'), (6, 'Kartikey Tripathi'), (100, 'Khushank Raj'), (24, 'Khushi Jain'), (77, 'Kuldeep Singh Malik'), (119, 'Lakhin Gupta'), (111, 'Lakshay Grover'), (113, 'Lakshay Sharma'), (18, 'Maniraj Singh Jadaun'), (63, 'Marshall Gaurav'), (108, 'Mayank Jain'), (15, 'Mayank Khanduja'), (26, 'Mukesh Garg'), (142, 'Mukesh Sharma'), (96, 'Neeraj Kumar'), (61, 'Nimit Pahwa'), (79, 'Nishant Rajput'), (44, 'Nitasha Bhatia'), (5, 'Nitesh Rai'), (99, 'Nitin Mishra'), (7, 'Nitish Arora'), (33, 'Ojasvee Bhardwaj'), (128, 'Palak Joshi'), (103, 'Phinehas Ratnam'), (65, 'Prabhupada Mohanty'), (48, 'Prachi Garg'), (37, 'Prapti Gupta'), (49, 'Prerna Sharma'), (139, 'Priya Mittal'), (40, 'Pulkit Goel'), (16, 'Rahul Gaur'), (69, 'Rahul Kumar Jha'), (14, 'Rajat Chaudhary'), (20, 'Rajeev Jha'), (78, 'Raunak Sett'), (145, 'Richa Gupta'), (32, 'Rishi Dhamija'), (114, 'Rizwan Ali'), (147, 'Rohan Kumar'), (56, 'Rohan Tyagi'), (50, 'Rohit Kumar'), (81, 'Sagar Bansal'), (98, 'Sahil Bhatia'), (109, 'Sahil Khan'), (84, 'Sahil Singh'), (74, 'Saloni Garg'), (133, 'Saloni Garg'), (19, 'Sameer Kumar'), (127, 'Sanil Khurana'), (125, 'Sankarshan Kohli'), (82, 'Sawal Kalra'), (121, 'Sawal Kalra'), (66, 'Sharad Gaur'), (122, 'Shibam Mukherjee'), (146, 'Shiv Aggarwal'), (68, 'Shivam Agarwal'), (135, 'Shivangi Jain'), (144, 'Shlagha Gulati'), (10, 'Shourye Jain'), (124, 'Shreya Jain'), (123, 'Shreya Vijhani'), (34, 'Shreyans Jain'), (136, 'Shruti Jain'), (55, 'Shubh Dhawan'), (13, 'Shubham Garg'), (17, 'Shubham Goria'), (97, 'Shubhangi Gupta'), (110, 'Siddharth Sethi'), (129, 'Soumya Kohli'), (31, 'SriShti ShaRma'), (27, 'Srijit S Madhavan'), (83, 'Suman Saurav Sharma'), (134, 'Sumit Arora'), (120, 'Sumit Malik'), (58, 'Swarndeep Singh'), (117, 'Syed Ahsan Shahid'), (57, 'S\xc3\xa0rth\xc3\xa2k Kh\xc3\xa1\xc3\xb1d\xc3\xaalw\xc3\xa3l'), (21, 'Tanseer Saji'), (73, 'Taran Deep'), (51, 'Tushar Ahuja'), (36, 'Tushar Sapra'), (80, 'UdIt MiTtal'), (132, 'Umang Khandelwal'), (90, 'Vaibhav Suri'), (143, 'Vatsal Papne'), (4, 'Vibhu Kesar'), (107, 'Vikrant Barul'), (88, 'Vishal Dharan'), (39, 'Viswajith Vellanki'), (70, 'Yugansh Tyagi'), (47, '\xc3\u0192fyie')], max_length=483),
        ),
    ]
