===============================
Croatia accounting localisation
===============================

.. |badge1| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

|badge1|

This module is base accounting localisation for Croatia
Primary target is to adjust odoo journals to Croatia out invoice fiskal rules
according to : https://www.zakon.hr/z/548/Zakon-o-fiskalizaciji-u-prometu-gotovinom

Configuration
=============

All out invoices in Croatia has strictly defined out invoice fiscal number structure/forming rules.
Important rules:
- invoice number consists of 3 parts:
  - AA - invoice number - strictly NO preceeding zeroes
  - BB - Business premisse code - alphanumerical chars
  - CC - PoS device code - strictly integer
  - Fiskal separator - only "/" or "-" allowed chars

This module manages Invoicing related data: Journals and Invoice sequence
automaticly according to localisation needs

Steps to setup invoicing according to Croatia Laws and regulation
1. Define fiskal separator ( on Company form, defaaulted to "/" so if it is acceptable, you may skip this step )
2. Invoicing >> Configuration >> Croatia specific settings >> Business premises

   - 2.1. - Create business premisse
   - 2.2. - Define invoicing sequence for premisse
     - Base on premisse or base on PoS device
   - 2.3 - Add Pos Device

  Based on selected settings you may select existing Journal(s) and sequences,
   Or, just activate Pos Devices needed, and finaly Business premisse

  If no journal is assigned for PoS device, one will be created
  Fiscal account invoice sequences will be created and assigned

  Fiskal sequences created and/or used are visible on Company - Croatia settings
