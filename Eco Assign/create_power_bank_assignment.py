#!/usr/bin/env python3
"""
Generate Power Bank Microeconomics Assignment - Complete .DOC File
Enhanced with Perplexity Deep Research Data
"""

from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_shading(cell, fill_color):
    """Set cell background color"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), fill_color)
    cell._tc.get_or_add_tcPr().append(shading_elm)

def create_document():
    doc = Document()

    # Set up page margins (1 inch top, right, bottom; 1.5 inch left)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.5)
        section.right_margin = Inches(1)
        section.page_height = Cm(29.7)  # A4
        section.page_width = Cm(21)     # A4

    # Add page numbers
    add_page_numbers(doc)

    # ==================== COVER PAGE ====================
    # Add spacing at top
    for _ in range(6):
        doc.add_paragraph()

    # Title
    title = doc.add_paragraph()
    title_run = title.add_run("MICROECONOMICS PRODUCT ASSIGNMENT")
    title_run.bold = True
    title_run.font.size = Pt(18)
    title_run.font.name = 'Times New Roman'
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    # Product Name
    product = doc.add_paragraph()
    product_run = product.add_run("POWER BANK")
    product_run.bold = True
    product_run.font.size = Pt(24)
    product_run.font.name = 'Times New Roman'
    product.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()
    doc.add_paragraph()

    # Subtitle
    subtitle = doc.add_paragraph()
    subtitle_run = subtitle.add_run("A Microeconomic Analysis of Production, Cost, Demand, and Market Dynamics")
    subtitle_run.italic = True
    subtitle_run.font.size = Pt(14)
    subtitle_run.font.name = 'Times New Roman'
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for _ in range(8):
        doc.add_paragraph()

    # Student Details Section
    details = [
        ("Name:", "[Student Name]"),
        ("Roll No:", "[Roll Number]"),
        ("Class:", "MMS Batch 25-27"),
        ("Semester:", "1st"),
        ("Academic Year:", "2025-2026"),
        ("Institute's Name:", "Sydenham Institute of Management Studies,"),
        ("", "Research and Entrepreneurship Education, Mumbai")
    ]

    for label, value in details:
        para = doc.add_paragraph()
        if label:
            label_run = para.add_run(label + " ")
            label_run.bold = True
            label_run.font.size = Pt(12)
            label_run.font.name = 'Times New Roman'
        value_run = para.add_run(value)
        value_run.font.size = Pt(12)
        value_run.font.name = 'Times New Roman'
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Page break after cover
    doc.add_page_break()

    # ==================== 1. INTRODUCTION AND EVOLUTION ====================
    add_heading(doc, "1. INTRODUCTION AND EVOLUTION", level=1)

    intro_text = """A power bank, also known as a portable charger or external battery pack, is a portable device that stores electrical energy and can be used to charge electronic devices such as smartphones, tablets, laptops, and wearables when access to a wall outlet is unavailable. According to market research, the global power bank market was valued at USD 12.2-15.6 billion in 2024, with India's power bank market reaching USD 963.31 million in the same year. Power banks have become indispensable accessories in the modern digital age, addressing the critical need for uninterrupted mobile connectivity and device functionality in an increasingly smartphone-dependent society."""
    add_justified_paragraph(doc, intro_text)

    # 1.1 Evolution of Power Bank Technology
    add_heading(doc, "1.1 Historical Evolution of Power Banks", level=2)

    evolution_text = """The evolution of power banks parallels the development of portable electronics and battery technology. The concept of portable power storage emerged in the early 2000s when mobile phones began requiring frequent charging due to increasing functionality and processing demands.

Early Era (2001-2008): The first commercial power banks appeared around 2001, utilising nickel-metal hydride (NiMH) batteries with limited energy density of approximately 60-80 Wh/kg. These early devices were bulky, heavy, and offered limited capacity, typically ranging from 1,000 to 2,000 mAh. They primarily served business travellers and early smartphone adopters who required extended battery life.

Lithium-Ion Revolution (2008-2014): The widespread adoption of lithium-ion (Li-ion) battery technology transformed the power bank industry with energy density improvements to 150-200 Wh/kg. Lithium-ion cells offered significantly higher energy density, lighter weight, and longer cycle life (500-1000 cycles) compared to NiMH alternatives. This period witnessed the emergence of major brands such as Anker, Xiaomi, and Ambrane, which standardised designs and improved affordability.

Fast Charging Era (2014-2020): The introduction of Quick Charge technology by Qualcomm (Quick Charge 2.0 in 2014, Quick Charge 3.0 in 2016) and USB Power Delivery standards revolutionised charging speeds. Power banks evolved to support 18W, 25W, and eventually 65W fast charging, significantly reducing charging times from 3-4 hours to under 30 minutes for compatible devices.

Current Era (2020-Present): Modern power banks incorporate multiple technologies including Qi wireless charging (5-15W), solar panels for emergency charging, USB-C Power Delivery up to 100W, and smart power management systems with microcontroller-based charge optimization. Capacities have expanded to 30,000 mAh and beyond, with some models capable of charging laptops multiple times. Lithium-polymer batteries now offer improved safety profiles and flexible form factors."""
    add_justified_paragraph(doc, evolution_text)

    # 1.2 Types and Versions
    add_heading(doc, "1.2 Types and Versions of Power Banks", level=2)

    types_text = """Power banks have diversified into several categories based on capacity, technology, and use cases:

Standard Power Banks: Basic models ranging from 5,000 to 20,000 mAh capacity, featuring USB-A output ports and micro-USB/USB-C input charging. These serve the mass market segment and are priced between Rs. 500-2,000, representing approximately 60% of total market volume.

Fast Charging Power Banks: Equipped with Qualcomm Quick Charge (QC 3.0/4.0) or USB Power Delivery (PD 3.0) technology, offering charging speeds of 18W to 65W. These command premium pricing between Rs. 1,500-5,000 and constitute the fastest-growing segment with 15-20% annual growth.

Wireless Power Banks: Integrated with Qi wireless charging technology, allowing cable-free charging at 5W-15W for compatible devices. Typically priced between Rs. 1,500-4,000, these appeal to consumers seeking convenience over charging speed.

Solar Power Banks: Incorporating photovoltaic panels (typically 5-20W capacity) for solar charging capability, primarily targeted at outdoor enthusiasts and emergency preparedness. Prices range from Rs. 1,500-6,000, though solar charging remains supplementary due to extended charging times (20-40 hours for full charge).

High-Capacity Power Banks: Ranging from 20,000 to 50,000 mAh, designed for heavy users, travellers, and laptop charging applications. Priced between Rs. 2,500-10,000, these often feature multiple output ports and support 60-100W Power Delivery for laptop charging."""
    add_justified_paragraph(doc, types_text)

    # 1.3 Product Classification
    add_heading(doc, "1.3 Product Classification: Sunrise, Sunset, or Evergreen?", level=2)

    classification_text = """Power banks should be classified as an evergreen product with strong sunrise characteristics. This classification is justified by the following market data and economic factors:

Evergreen Justification: The fundamental need for portable power stems from humanity's increasing dependence on mobile electronic devices. With global smartphone users exceeding 6.8 billion in 2024 and average daily smartphone usage reaching 4.5 hours, the demand for portable charging solutions remains constant regardless of technological evolution. The problem of limited battery life in mobile devices persists despite advancements in battery technology, ensuring sustained baseline demand.

Sunrise Characteristics: India's power bank market is projected to grow from USD 963.31 million in 2024 to USD 2,565.50 million by 2033, representing a robust Compound Annual Growth Rate (CAGR) of 11.5%. The global market demonstrates similar growth patterns with 6.1%-8.1% CAGR projections through 2030. The emergence of wireless charging, gallium nitride (GaN) technology for compact high-power designs, graphene batteries promising 5x faster charging, and smart power management systems represents expanding market frontiers.

Growth Drivers: Key factors supporting continued market expansion include increasing smartphone penetration in tier-2 and tier-3 cities, growing adoption of multiple electronic devices per user (smartwatches, wireless earbuds, tablets), expansion of electric vehicle charging accessories, and rising demand from the gaming and content creation communities requiring extended device usage.

The market demonstrates consistent year-over-year growth, with festive season sales (Diwali, New Year) showing 40-60% spikes in demand, confirming the product's evergreen nature with growth characteristics."""
    add_justified_paragraph(doc, classification_text)

    doc.add_page_break()

    # ==================== 2. BACKEND ANALYSIS ====================
    add_heading(doc, "2. BACKEND ANALYSIS: PRODUCTION AND COST ECONOMICS", level=1)

    # 2.1 Production Modality
    add_heading(doc, "2.1 Production Modality and Technology", level=2)

    production_text = """Power bank manufacturing involves a multi-stage assembly process combining battery cell production, electronic circuit assembly, and housing fabrication. The production process has evolved significantly with increasing automation and quality control standards.

Battery Cell Assembly: The core component of power banks is the lithium-ion or lithium-polymer battery cell. Manufacturing involves electrode coating with lithium cobalt oxide (LiCoO2) or lithium iron phosphate (LiFePO4), cell stacking or winding, electrolyte filling, and formation cycling. Major cell manufacturers operate in China (CATL, BYD - 60% global share), South Korea (Samsung SDI, LG Energy Solution - 25%), and Japan (Panasonic - 10%), with these companies dominating global production.

PCB Assembly: The Printed Circuit Board (PCB) controls charging and discharging functions, incorporating power management ICs (typically from Texas Instruments, Qualcomm), protection circuits for overcharge/over-discharge/short-circuit protection, and charging protocol controllers supporting QC/PD standards. Surface Mount Technology (SMT) lines enable high-volume production with precision component placement at speeds of 25,000-50,000 components per hour.

Final Assembly: Battery cells are connected in parallel configurations to achieve desired capacity, wrapped with protective PVC/heat-shrink materials, and installed within ABS plastic or aluminum alloy housings. Quality testing includes capacity verification (discharge testing to 3.0V cutoff), charging cycle tests (minimum 500 cycles to 80% capacity), thermal testing (-10°C to +45°C operating range), and safety compliance checks per BIS IS 17018:2018 standards.

Technological Evolution: Manufacturing has transitioned from labour-intensive assembly (15-20 workers per 1000 units) to automated production lines (3-5 workers per 1000 units). Modern facilities employ robotic pick-and-place assembly, automated optical inspection (AOI), and computerised battery grading systems. This technological progression has reduced per-unit labour costs by 40-60% while improving product consistency and safety standards."""
    add_justified_paragraph(doc, production_text)

    # 2.2 Raw Materials and Factor Market
    add_heading(doc, "2.2 Raw Materials and Factor Market", level=2)

    materials_text = """Power bank manufacturing relies on diverse raw materials and components sourced from global supply chains:"""
    add_justified_paragraph(doc, materials_text)

    # Raw Materials Table
    table = doc.add_table(rows=8, cols=4)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    headers = ['Component', 'Source Region', 'Cost per Unit (USD)', 'Cost Nature']
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        set_cell_shading(cell, 'D9E2F3')
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)

    # Data rows from Perplexity research
    materials_data = [
        ('Lithium-ion/Polymer Cells', 'China, S. Korea, Japan', '$2.50-4.00', 'Variable'),
        ('PCB & Power Management IC', 'China, Taiwan', '$1.50-2.50', 'Variable'),
        ('ABS/Aluminum Housing', 'Domestic (India)/China', '$1.00-2.00', 'Variable'),
        ('USB Ports & Connectors', 'China', '$0.50-1.00', 'Variable'),
        ('LED Indicators & Displays', 'China', '$0.30-0.50', 'Variable'),
        ('Cables & Accessories', 'China, Domestic', '$0.40-0.80', 'Variable'),
        ('Packaging & Manuals', 'Local Suppliers', '$0.50-1.00', 'Variable')
    ]

    for i, row_data in enumerate(materials_data, 1):
        for j, cell_text in enumerate(row_data):
            cell = table.rows[i].cells[j]
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(10)

    doc.add_paragraph()

    materials_detail = """Lithium-Ion Battery Cells: Constitute 35-45% of total product cost at $2.50-4.00 per 10,000 mAh capacity. Cells are predominantly imported from China (70%), with premium brands using Samsung SDI or LG cells from South Korea. Lithium is primarily sourced from Australia (52% global supply), Chile (25%), and China (13%), while cobalt comes from the Democratic Republic of Congo (70% global supply), creating supply chain concentration risks.

PCBs and Electronic Components: Power management integrated circuits (PMICs) and protection circuits cost $1.50-2.50 per unit and are manufactured predominantly in China and Taiwan. Key semiconductor suppliers include Texas Instruments, Qualcomm (for Quick Charge licensing), and domestic alternatives from MediaTek. These components control voltage regulation (5V/9V/12V output), overcharge protection (4.2V cutoff), and charging protocols.

Housing Materials: ABS (Acrylonitrile Butadiene Styrene) plastic housings cost $1.00-2.00 per unit, while premium aluminum alloy enclosures command $2.00-4.00. Domestic polymer suppliers like Reliance Industries and IPCL provide raw granules at Rs. 120-150/kg, while injection moulding is performed in manufacturing clusters across Noida, Shenzhen, and Dongguan with typical cycle times of 30-45 seconds per unit."""
    add_justified_paragraph(doc, materials_detail)

    # 2.3 Cost Structure
    add_heading(doc, "2.3 Cost Structure Analysis", level=2)

    cost_intro = """Understanding the cost structure of power bank manufacturing is essential for pricing decisions and profitability analysis. Based on industry data, the total variable cost per 10,000 mAh power bank ranges from $7.20 to $12.00 (approximately Rs. 600-1,000), with raw materials constituting the largest cost component."""
    add_justified_paragraph(doc, cost_intro)

    # Capital Expenditure
    capex_text = """Capital Expenditure (CapEx): Establishing a power bank manufacturing facility requires significant upfront investment in machinery and infrastructure:

Small-Scale Assembly Unit: Rs. 20-40 lakhs (manual assembly with basic testing equipment, capacity 5,000-10,000 units/month)
Medium-Scale Factory: Rs. 75 lakhs - 2 crores (semi-automated SMT lines, capacity 50,000-100,000 units/month)
Large-Scale Manufacturing: Rs. 5-15 crores (fully automated production with in-house cell assembly and BIS-certified testing labs, capacity 500,000+ units/month)"""
    add_justified_paragraph(doc, capex_text)

    # Cost Table
    doc.add_paragraph()
    cost_heading = doc.add_paragraph()
    cost_heading_run = cost_heading.add_run("Table 2: Detailed Cost Breakdown per 10,000 mAh Power Bank")
    cost_heading_run.bold = True
    cost_heading_run.font.name = 'Times New Roman'
    cost_heading_run.font.size = Pt(11)
    cost_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

    cost_table = doc.add_table(rows=12, cols=4)
    cost_table.style = 'Table Grid'
    cost_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    cost_headers = ['Cost Component', 'USD', 'INR (approx.)', 'Percentage']
    for i, header in enumerate(cost_headers):
        cell = cost_table.rows[0].cells[i]
        cell.text = header
        set_cell_shading(cell, 'D9E2F3')
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)

    # Cost data from Perplexity research
    cost_data = [
        ('Battery Cells (Li-ion/LiPo)', '$2.50-4.00', 'Rs. 210-335', '35-40%'),
        ('PCB & Power Management', '$1.50-2.50', 'Rs. 125-210', '18-22%'),
        ('Housing (ABS/Aluminum)', '$1.00-2.00', 'Rs. 85-170', '12-15%'),
        ('USB Ports & Connectors', '$0.50-1.00', 'Rs. 40-85', '6-8%'),
        ('LED/Display Components', '$0.30-0.50', 'Rs. 25-40', '3-4%'),
        ('Cables & Accessories', '$0.40-0.80', 'Rs. 35-65', '5-6%'),
        ('Packaging Materials', '$0.50-1.00', 'Rs. 40-85', '5-7%'),
        ('Labour & Assembly', '$0.30-0.60', 'Rs. 25-50', '4-5%'),
        ('Quality Testing & QC', '$0.20-0.40', 'Rs. 17-35', '2-3%'),
        ('Overheads & Depreciation', '$0.50-0.80', 'Rs. 40-65', '6-8%'),
        ('Total Variable Cost', '$7.20-12.00', 'Rs. 600-1,000', '100%')
    ]

    for i, row_data in enumerate(cost_data, 1):
        for j, cell_text in enumerate(row_data):
            cell = cost_table.rows[i].cells[j]
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(10)
            if i == 11:  # Total row
                set_cell_shading(cell, 'E2EFDA')
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True

    doc.add_paragraph()

    # Cost Curves Description
    cost_curves_text = """Average Cost and Marginal Cost Analysis:

The power bank industry demonstrates significant economies of scale, where Average Cost (AC) decreases as production volume increases due to the spreading of fixed costs over larger output quantities. Industry data indicates that average cost per unit decreases by approximately 15-20% when production doubles from 10,000 to 20,000 units monthly.

The typical U-shaped Average Cost curve applies, with:
- Declining AC phase (0-50,000 units/month): Fixed costs spread across increasing output
- Minimum AC point (50,000-100,000 units/month): Optimal production scale for cost efficiency
- Rising AC phase (>150,000 units/month): Coordination inefficiencies and capacity constraints

Marginal Cost (MC) remains relatively stable in the relevant production range at $6.50-8.00 per unit, as variable costs (primarily battery cells and components) maintain proportional relationships with output. The MC curve intersects the AC curve at the minimum point of AC, representing the optimal production scale.

For a typical medium-scale manufacturer producing 50,000 units monthly:
- Average Fixed Cost (AFC): Rs. 80-120 per unit
- Average Variable Cost (AVC): Rs. 600-800 per unit
- Average Total Cost (ATC): Rs. 680-920 per unit
- Marginal Cost (MC): Rs. 550-700 per additional unit"""
    add_justified_paragraph(doc, cost_curves_text)

    # 2.4 Supply Chain Analysis
    add_heading(doc, "2.4 Supply Chain Analysis", level=2)

    supply_chain_text = """The power bank supply chain operates through distinct backend and frontend networks spanning multiple countries and intermediaries:

Backend Supply Chain (Manufacturing to Distribution):

Tier 1 - Raw Material Suppliers: Global battery cell manufacturers (CATL, BYD from China; Samsung SDI, LG Energy Solution from Korea), lithium miners (Albemarle, SQM from Chile/Australia), electronic component suppliers (Texas Instruments, Qualcomm), and polymer raw material providers form the foundational supply tier. Lead times range from 4-8 weeks for standard components to 12-16 weeks for custom battery configurations.

Tier 2 - Component Manufacturers: Companies specialising in PCB assembly (Foxconn, Pegatron), housing moulding (domestic injection moulding units), and cable manufacturing convert raw materials into sub-assemblies ready for final integration. These operate primarily in Shenzhen, Dongguan (China), and Noida, Greater Noida (India).

Tier 3 - Final Assembly: Original Equipment Manufacturers (OEMs) such as Xiaomi, Samsung, and Anker, along with Original Design Manufacturers (ODMs) like Sunwoda and Scud Group, integrate components into finished power banks. Major assembly hubs include Shenzhen (China - 65% global production), Noida-Greater Noida (India - growing domestic manufacturing), and Vietnam (emerging hub for cost-competitive production).

Frontend Supply Chain (Distribution to Consumer):

Manufacturers distribute through multiple channels with varying margin structures:
- National Distributors: Brands like Xiaomi, Ambrane, and Portronics use regional distributors covering multiple states, with distributor margins of 8-12%
- E-commerce Platforms: Amazon (35% market share), Flipkart (30%), and brand D2C websites facilitate direct-to-consumer sales with platform commissions of 5-15%
- Modern Retail Chains: Electronics retailers (Croma, Vijay Sales, Reliance Digital) maintain physical store presence with retailer margins of 18-25%
- Wholesale Markets: Markets like Gaffar Market (Delhi), Lamington Road (Mumbai), and SP Road (Bangalore) serve small retailers and bulk buyers at 15-25% below MRP"""
    add_justified_paragraph(doc, supply_chain_text)

    # 2.5 Government Policies
    add_heading(doc, "2.5 Government Policies and Regulations", level=2)

    govt_policy_text = """Government intervention significantly influences the power bank industry through taxation, safety standards, and environmental regulations:

Goods and Services Tax (GST): Power banks are classified under HSN code 8507 (Electric Accumulators) and attract 18% GST. This relatively high tax rate impacts final retail prices, adding approximately Rs. 150-300 to a Rs. 1,000-1,500 power bank. Input tax credit mechanisms allow manufacturers to offset GST paid on raw materials against output tax liability.

Bureau of Indian Standards (BIS): BIS certification is mandatory for power banks sold in India under IS 17018:2018 specifications. This standard mandates comprehensive safety requirements including:
- Overcharge protection (voltage cutoff at 4.25V per cell)
- Over-discharge protection (cutoff at 2.75V per cell)
- Short circuit protection (response time <100 microseconds)
- Thermal management (operating range -10°C to +45°C)
- Drop test compliance (1.0 metre height, 6 surfaces)
Compliance involves testing fees of Rs. 50,000-1,50,000 per model and annual surveillance audits, increasing production costs by 2-4% but ensuring consumer safety and market legitimacy.

Battery Waste Management Rules, 2022: Under these updated regulations, manufacturers bear Extended Producer Responsibility (EPR) for collection and recycling of lithium-ion batteries. Compliance requires:
- Registration with Central Pollution Control Board (CPCB)
- Collection targets of 70% by 2024-25, increasing to 80% by 2026-27
- Partnership with authorized recyclers
- Filing quarterly returns on battery sales and collection
This adds 2-4% to operational costs but supports circular economy objectives.

Import Duties and Make in India: Basic Customs Duty (BCD) of 15% applies to finished power banks and 5-10% on components. The phased manufacturing program incentivizes domestic value addition, with reduced duties for components when final assembly occurs in India. Production Linked Incentive (PLI) Scheme for Advanced Chemistry Cell (ACC) batteries allocated Rs. 18,100 crores to develop domestic battery manufacturing capability."""
    add_justified_paragraph(doc, govt_policy_text)

    doc.add_page_break()

    # ==================== 3. FRONTEND ANALYSIS ====================
    add_heading(doc, "3. FRONTEND ANALYSIS: MARKET DEMAND AND REVENUE DYNAMICS", level=1)

    # 3.1 Demand Analysis
    add_heading(doc, "3.1 Nature of Demand", level=2)

    demand_text = """The demand for power banks demonstrates characteristics of both normal goods and complementary goods, with demand patterns influenced by multiple economic and behavioural factors.

Market Size and Growth: India's power bank market reached USD 963.31 million in 2024 and is projected to grow to USD 2,565.50 million by 2033, representing an 11.5% CAGR. The global market, valued at USD 12.2-15.6 billion in 2024, is expected to grow at 6.1-8.1% CAGR through 2030.

Nature of Demand: Power bank demand is derived demand, fundamentally dependent on smartphone and portable electronics ownership. With India's smartphone user base exceeding 750 million in 2024, power bank demand rises correspondingly. The product serves as a complementary good to smartphones, tablets, wireless earbuds, and smartwatches.

Determinants of Demand:

1. Price of the Product: Lower prices stimulate higher demand, particularly in price-sensitive Indian market segments. Budget power banks (Rs. 500-1,000) witness 3-4x higher sales volumes compared to premium segments (Rs. 2,000+).

2. Consumer Income: Power banks exhibit positive income elasticity. Rising disposable incomes, particularly among urban middle-class consumers (monthly income Rs. 50,000+), increase demand for higher-capacity (20,000+ mAh) and feature-rich models with fast charging capabilities.

3. Price of Related Goods: Declining smartphone prices (average selling price reduced from Rs. 15,000 to Rs. 12,000 over 2020-2024) expand the consumer base requiring charging accessories. New device launches by Apple, Samsung, and Xiaomi consistently boost power bank sales.

4. Consumer Preferences: Growing brand consciousness (branded products command 25-30% premium over unbranded), environmental awareness (demand for recyclable batteries increasing 15% annually), and feature preferences (fast charging adoption growing at 20% annually) shape demand patterns.

5. Seasonal Patterns: Demand peaks during festive seasons (Diwali, New Year - 40-60% volume spike), back-to-school periods (June-July - 25% increase), and during major e-commerce sales events (Amazon Prime Day, Flipkart Big Billion Days - 80-100% daily volume increase)."""
    add_justified_paragraph(doc, demand_text)

    # 3.2 Elasticity of Demand
    add_heading(doc, "3.2 Elasticity of Demand Analysis", level=2)

    elasticity_text = """Understanding demand elasticity is crucial for pricing strategy and revenue optimisation in the power bank market. Research indicates specific elasticity values that guide business decisions.

Price Elasticity of Demand (PED):

The power bank market exhibits moderately elastic demand with PED values ranging from -0.8 to -1.2 based on market segment analysis:

1. Budget Segment (Rs. 500-1,000): PED approximately -1.3 to -1.5 (elastic)
   - High substitutability with unbranded alternatives
   - Price-sensitive consumer base
   - 10% price reduction leads to 13-15% quantity increase

2. Mid-Range Segment (Rs. 1,000-2,000): PED approximately -0.9 to -1.1 (unit elastic)
   - Moderate brand loyalty
   - Feature differentiation provides some insulation
   - 10% price reduction leads to 9-11% quantity increase

3. Premium Segment (Rs. 2,000+): PED approximately -0.6 to -0.8 (relatively inelastic)
   - Strong brand loyalty (Apple, Samsung accessories)
   - Unique features justify premium pricing
   - 10% price reduction leads to only 6-8% quantity increase

Factors contributing to elastic demand:
- Availability of multiple substitute brands and unbranded options
- Non-essential nature of the product (can defer purchase)
- Transparent pricing through e-commerce comparison
- Low switching costs between brands

Income Elasticity of Demand (YED):

Power banks demonstrate positive income elasticity of +0.95 to +1.15, classifying them as normal goods with near-unitary income sensitivity:
- YED of +0.95 to +1.05 for basic power banks (necessity-like behaviour)
- YED of +1.05 to +1.15 for premium/feature-rich models (mild luxury characteristics)

As household income increases by 10%, power bank demand increases by approximately 9.5-11.5%, with consumers upgrading from basic to premium models with higher capacity and advanced features.

Cross-Price Elasticity (XED):

Power banks exhibit varied cross-price relationships:
- Smartphones: XED = -0.3 to -0.5 (complementary goods - smartphone price decrease increases power bank demand)
- Car chargers: XED = +0.2 to +0.4 (substitute goods)
- Wireless chargers: XED = +0.1 to +0.3 (partial substitutes)"""
    add_justified_paragraph(doc, elasticity_text)

    # Add demand curve description
    demand_curve_text = """Demand Curve Characteristics:

The demand curve for power banks slopes downward from left to right, consistent with the law of demand. At higher prices, quantity demanded decreases as consumers defer purchases or switch to alternatives. The curve's slope (relatively flat in budget segments, steeper in premium segments) reflects varying elasticity across market segments.

For individual brands operating under monopolistic competition, the demand curve (Average Revenue curve) slopes downward with the following characteristics:
- Relatively elastic portion at higher prices (consumers switch to competitors)
- Relatively inelastic portion at lower prices (loyal customer base)
- Kinked demand curve possibility in oligopolistic premium segment

The Marginal Revenue (MR) curve lies below the demand curve (AR), with MR = AR × (1 - 1/|PED|). For PED of -1.2, MR equals approximately 0.17 × AR, indicating significant revenue impact from price reductions."""
    add_justified_paragraph(doc, demand_curve_text)

    # 3.3 Market Structure
    add_heading(doc, "3.3 Market Structure Analysis", level=2)

    market_structure_text = """The Indian power bank market operates under monopolistic competition, characterised by the following features:

Many Sellers with Differentiated Products: Numerous manufacturers compete in the market with varying market shares:
- Xiaomi/Mi: 18-22% market share (market leader)
- Anker: 12-15% (premium segment leader)
- Samsung: 8-10% (brand ecosystem loyalty)
- Ambrane: 7-9% (value segment)
- Portronics: 5-7%
- Realme/OnePlus: 6-8% combined
- Others (including unbranded): 35-40%

Product Differentiation: While functionally similar, power banks are differentiated through:
- Capacity variations (5,000 mAh to 30,000 mAh)
- Charging technology (standard 5V/2A, Quick Charge 3.0/4.0, Power Delivery 3.0)
- Form factors (slim 10mm, rugged IP67-rated, compact credit-card sized)
- Additional features (wireless charging, LED displays, solar panels, built-in cables)
- Brand image and after-sales service (1-year to 18-month warranty)

Low Barriers to Entry: The industry exhibits relatively low entry barriers:
- Moderate capital requirements (Rs. 20-50 lakhs for small-scale assembly)
- Available ODM/OEM contract manufacturing
- Established e-commerce distribution channels
- BIS certification requirement (creates some regulatory barrier)

Non-Price Competition: Firms engage in substantial non-price competition:
- Advertising expenditure: 8-15% of revenue
- Product design innovation (slimmer, lighter, faster-charging)
- Extended warranty offerings (12-18 months)
- Celebrity endorsements (Xiaomi with tech influencers)
- Social media marketing and influencer partnerships
- E-commerce exclusive launches and flash sales"""
    add_justified_paragraph(doc, market_structure_text)

    # 3.4 Pricing Mechanism
    add_heading(doc, "3.4 Pricing Mechanism", level=2)

    pricing_text = """Power bank pricing follows cost-plus and competitive pricing strategies across the value chain:

Wholesale Pricing: Manufacturers sell to distributors at ex-factory prices plus margin. Typical manufacturer margins range from 25-40% over production costs. Distributors receive 8-12% margin on wholesale transactions.

Retail Pricing: Retailers apply 18-25% markup over wholesale prices. E-commerce platforms operate on lower margins (8-15%) due to reduced overhead costs but charge commission fees (5-15%) to sellers."""
    add_justified_paragraph(doc, pricing_text)

    # Pricing Table
    pricing_table_heading = doc.add_paragraph()
    pricing_heading_run = pricing_table_heading.add_run("Table 3: Pricing Structure for 10,000 mAh Fast-Charging Power Bank")
    pricing_heading_run.bold = True
    pricing_heading_run.font.name = 'Times New Roman'
    pricing_heading_run.font.size = Pt(11)
    pricing_table_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

    pricing_table = doc.add_table(rows=9, cols=2)
    pricing_table.style = 'Table Grid'
    pricing_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    pricing_headers = ['Stage', 'Price (Rs.)']
    for i, header in enumerate(pricing_headers):
        cell = pricing_table.rows[0].cells[i]
        cell.text = header
        set_cell_shading(cell, 'D9E2F3')
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)

    pricing_data = [
        ('Total Variable Cost (Production)', '600-850'),
        ('Fixed Cost Allocation per unit', '80-120'),
        ('Ex-Factory Cost', '680-970'),
        ('Manufacturer Margin (30%)', '205-290'),
        ('Manufacturer Selling Price', '885-1,260'),
        ('Distributor Margin (10%)', '90-125'),
        ('Retailer Margin (20%)', '195-275'),
        ('MRP (inclusive of 18% GST)', '1,299-1,799')
    ]

    for i, row_data in enumerate(pricing_data, 1):
        for j, cell_text in enumerate(row_data):
            cell = pricing_table.rows[i].cells[j]
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(11)

    doc.add_paragraph()

    # 3.5 Revenue Analysis
    add_heading(doc, "3.5 Revenue Analysis", level=2)

    revenue_text = """Revenue distribution across the power bank value chain involves multiple stakeholders, with manufacturers capturing the largest absolute value:

Manufacturer Revenue: Manufacturers earn gross margins of 25-40% on ex-factory sales, translating to net margins of 8-15% after operating expenses. For a typical manufacturer selling 100,000 units monthly at Rs. 900 average selling price, monthly revenue approximates Rs. 9 crores with gross profit of Rs. 2.5-3.5 crores.

Total Revenue (TR) and Average Revenue (AR) Analysis:
- TR = Price × Quantity
- AR = TR/Q = Price per unit
Under monopolistic competition, the demand curve (AR curve) slopes downward, indicating that increased sales require price reductions.

Marginal Revenue (MR):
- MR = ΔTR/ΔQ
- MR < AR due to the downward-sloping demand curve
- For PED = -1.2, MR = AR × (1 - 1/1.2) = 0.167 × AR
- Profit maximisation occurs where MR = MC

Revenue by Channel:
- E-commerce (Amazon, Flipkart): 45-50% of total industry revenue
- Modern retail (Croma, Reliance Digital): 20-25%
- Traditional retail & wholesale: 15-20%
- Direct-to-Consumer (brand websites): 8-12%"""
    add_justified_paragraph(doc, revenue_text)

    # Revenue Table
    revenue_table_heading = doc.add_paragraph()
    revenue_heading_run = revenue_table_heading.add_run("Table 4: Revenue Distribution by Value Chain Stakeholder")
    revenue_heading_run.bold = True
    revenue_heading_run.font.name = 'Times New Roman'
    revenue_heading_run.font.size = Pt(11)
    revenue_table_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

    revenue_table = doc.add_table(rows=6, cols=3)
    revenue_table.style = 'Table Grid'
    revenue_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    revenue_headers = ['Stakeholder', 'Margin Range', 'Share of Consumer Price']
    for i, header in enumerate(revenue_headers):
        cell = revenue_table.rows[0].cells[i]
        cell.text = header
        set_cell_shading(cell, 'D9E2F3')
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)

    revenue_data = [
        ('Manufacturer', '25-40%', '50-58%'),
        ('Distributor', '8-12%', '6-10%'),
        ('Retailer/E-commerce', '15-25%', '12-18%'),
        ('GST (Government)', '18%', '15-16%'),
        ('Logistics & Platform Fees', '3-8%', '3-6%')
    ]

    for i, row_data in enumerate(revenue_data, 1):
        for j, cell_text in enumerate(row_data):
            cell = revenue_table.rows[i].cells[j]
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(11)

    doc.add_paragraph()

    # 3.6 Selling and Marketing Costs
    add_heading(doc, "3.6 Selling and Marketing Costs", level=2)

    marketing_text = """Selling costs constitute a significant component of total costs in the monopolistically competitive power bank market, as firms attempt to differentiate products and build brand preference:

Advertising and Promotion (8-15% of revenue):
- Digital advertising (Google Ads, Facebook/Instagram): Rs. 5-15 per click, Rs. 100-300 per conversion
- Influencer marketing: Rs. 50,000-5,00,000 per campaign depending on influencer reach
- Television commercials: Rs. 2-10 lakhs per 30-second slot on major channels
- Social media content creation: Rs. 1-3 lakhs monthly

E-commerce Platform Costs (10-20% of selling price):
- Amazon commission: 5-15% depending on category
- Flipkart commission: 4-12%
- Fulfillment charges (FBA/FBF): Rs. 30-80 per unit
- Sponsored product advertising: Rs. 3-10 per click, 5-15% ACoS target

Distribution and Trade Marketing (8-12% of MRP):
- Distributor margins: 8-12%
- Retailer margins: 15-25%
- Point-of-sale displays: Rs. 5,000-20,000 per retail outlet
- Demo units and sampling: Rs. 500-1,000 per store

Packaging and Branding (Rs. 40-100 per unit):
- Premium packaging design and materials
- Instructional materials and warranty cards
- Branded cables and accessories
This investment enhances perceived value and supports premium pricing strategies."""
    add_justified_paragraph(doc, marketing_text)

    doc.add_page_break()

    # ==================== 4. SUGGESTIONS FOR IMPROVEMENT ====================
    add_heading(doc, "4. SUGGESTIONS FOR IMPROVING PRODUCTION AND DELIVERY EFFICIENCY", level=1)

    suggestions_text = """Based on the microeconomic analysis of the power bank industry, the following economically sound suggestions can enhance production efficiency, reduce costs, and improve market delivery:

1. Domestic Battery Cell Manufacturing: The most significant cost reduction opportunity lies in establishing domestic lithium-ion cell manufacturing under the PLI scheme for Advanced Chemistry Cells (Rs. 18,100 crore allocation). Currently, 70-80% of cells are imported from China, exposing manufacturers to currency fluctuations (USD/INR volatility of 5-8% annually) and supply chain disruptions. Backward integration into cell production could reduce raw material costs by 15-25% and improve supply security.

2. Supply Chain Optimisation through Technology: Implementing just-in-time (JIT) inventory management with real-time demand forecasting using AI/ML algorithms can reduce working capital requirements by 20-30%. Establishing vendor-managed inventory (VMI) arrangements with key component suppliers reduces stock-out risks and warehousing costs by 10-15%.

3. Direct-to-Consumer (D2C) Channel Development: Developing robust D2C e-commerce capabilities through brand websites eliminates distributor (8-12%) and retailer margins (15-25%), potentially reducing consumer prices by 20-30% while maintaining or improving manufacturer profitability. This requires investment in digital marketing (customer acquisition cost of Rs. 150-300), order management systems, and last-mile logistics partnerships.

4. Economies of Scale through Consolidation: Achieving production volumes of 100,000+ units monthly can reduce average costs by 15-20% through bulk procurement advantages, spread of fixed costs, and improved negotiating power with suppliers. Strategic partnerships or contract manufacturing arrangements with larger ODMs can achieve similar benefits without proportional capital investment.

5. Sustainable Manufacturing Practices: Adopting recycled ABS plastic (10-15% cheaper than virgin material), implementing energy-efficient LED lighting and solar panels in factories (reducing electricity costs by 20-30%), and establishing proactive battery recycling programmes addresses Battery Waste Management Rules compliance while reducing long-term operational costs and enhancing brand image among environmentally conscious consumers.

6. Quality-Driven Cost Reduction: Investing in automated quality control systems (AOI, computerised battery testing) can reduce defect rates from industry average of 2-3% to below 0.5%, significantly reducing warranty claims, returns processing costs, and reputation damage. The initial investment of Rs. 15-25 lakhs typically achieves payback within 12-18 months."""
    add_justified_paragraph(doc, suggestions_text)

    doc.add_page_break()

    # ==================== 5. LESSONS LEARNED ====================
    add_heading(doc, "5. LESSONS LEARNED", level=1)

    lessons_text = """Through this comprehensive microeconomic analysis of the power bank industry, I have gained valuable insights into the practical application of economic theories and concepts:

1. Understanding Cost Structure and Pricing Dynamics: I learned that the cost structure of a product fundamentally determines pricing flexibility and market positioning. The power bank industry's high variable cost ratio (raw materials comprising 55-65% of total costs) limits pricing power and necessitates volume-based strategies to achieve profitability. The detailed breakdown of costs from battery cells ($2.50-4.00) to packaging ($0.50-1.00) demonstrated how each component contributes to the final price consumers pay. This reinforced my understanding of how fixed and variable costs interact to determine average cost behaviour and optimal production scales.

2. Elasticity as a Strategic Decision-Making Tool: I discovered that demand elasticity varies significantly across market segments and directly influences pricing strategy. The price elasticity values of -0.8 to -1.2 across different segments explained why premium brands can maintain higher prices while budget brands must compete aggressively on price. The income elasticity of +0.95 to +1.15 confirmed power banks as normal goods with near-unitary income sensitivity. This practical application of elasticity concepts demonstrated how theoretical constructs guide real-world pricing decisions and revenue optimisation.

3. Market Structure and Competitive Dynamics: I observed how monopolistic competition shapes industry dynamics - numerous competitors (Xiaomi 18-22%, Anker 12-15%, and many others), product differentiation through features and branding, and non-price competition through advertising and innovation coexist despite low entry barriers. This analysis clarified why firms invest heavily in branding and marketing (8-15% of revenue) rather than engaging purely in price competition, validating Chamberlin's theory of monopolistic competition and the role of selling costs.

4. Supply Chain Economics and Value Distribution: I recognised that supply chain efficiency significantly impacts final product pricing and competitive positioning. The multi-tier distribution system introduces cumulative margins (8-12% distributor, 15-25% retailer) that substantially inflate consumer prices beyond manufacturing costs. Understanding that manufacturers capture 50-58% of consumer price while intermediaries and government (GST) share the remainder highlighted the economic rationale for direct-to-consumer models and vertical integration strategies.

5. Government Policy as Market Shaper: I understood how regulatory interventions (18% GST, BIS IS 17018:2018 certification, Battery Waste Management Rules 2022) create both challenges and opportunities. Compliance costs increase production expenses by 4-8%, but regulations also create entry barriers that benefit established players and ensure product quality standards that build consumer confidence. The PLI scheme's Rs. 18,100 crore allocation for battery manufacturing illustrated how industrial policy shapes competitive advantages and long-term market structure."""
    add_justified_paragraph(doc, lessons_text)

    # References Section
    doc.add_page_break()
    add_heading(doc, "REFERENCES", level=1)

    references_text = """1. Grand View Research (2024). Power Bank Market Size, Share & Trends Analysis Report.

2. Mordor Intelligence (2024). India Power Bank Market - Growth, Trends, and Forecasts.

3. Bureau of Indian Standards. IS 17018:2018 - Specification for Portable Secondary Lithium Cells and Batteries.

4. Central Board of Indirect Taxes and Customs. GST Rate Schedule for Electronic Products.

5. Ministry of Environment, Forest and Climate Change. Battery Waste Management Rules, 2022.

6. Ministry of Heavy Industries. Production Linked Incentive Scheme for Advanced Chemistry Cell Battery Storage.

7. Statista (2024). Smartphone Users in India 2024-2028.

8. IBEF (2024). Indian Electronics Industry Report.

9. International Energy Agency (2024). Global EV Outlook - Battery Technology Trends.

10. Research reports from Counterpoint Research, IDC, and Canalys on Indian smartphone and accessories market."""
    add_justified_paragraph(doc, references_text)

    return doc

def add_heading(doc, text, level=1):
    """Add a heading with proper formatting"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    para.space_before = Pt(12)
    para.space_after = Pt(6)

def add_justified_paragraph(doc, text):
    """Add a justified paragraph with proper formatting"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    para.paragraph_format.line_spacing = 1.5
    para.space_after = Pt(8)

def add_page_numbers(doc):
    """Add page numbers to footer"""
    for section in doc.sections:
        footer = section.footer
        footer.is_linked_to_previous = False
        para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Add page number field
        run = para.add_run()
        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')

        instrText = OxmlElement('w:instrText')
        instrText.text = "PAGE"

        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')

        run._r.append(fldChar1)
        run._r.append(instrText)
        run._r.append(fldChar2)

if __name__ == "__main__":
    print("Creating Enhanced Power Bank Microeconomics Assignment...")
    print("Incorporating Perplexity Deep Research Data...")
    doc = create_document()
    output_path = "/mnt/e/AI and Projects/MMS-Prep/Eco Assign/Power_Bank_Microeconomics_Assignment.docx"
    doc.save(output_path)
    print(f"Document saved successfully to: {output_path}")
    print("Assignment includes:")
    print("- Market statistics: India USD 963.31 Mn, 11.5% CAGR")
    print("- Detailed cost structure tables with USD/INR values")
    print("- Elasticity analysis: PED -0.8 to -1.2, YED +0.95 to +1.15")
    print("- Market share data: Xiaomi 18-22%, Anker 12-15%, etc.")
    print("- Government policies: GST 18%, BIS, Battery Waste Rules")
